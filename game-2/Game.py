class Game:
    def __init__(self):
        self._harry = None
        self._voldemort = None
        self._dementor = None
        # after defining platform class, we will add this
        # self._platform_heights = [0,1,2]
        self._vold_img_r = pygame.image.load("project\\voldemort.png")
        self._vold_img_r.set_colorkey((255,255,255))
        self._vold_img_l = pygame.image.load("project\\voldemort_l.png")
        self._vold_img_l.set_colorkey((255,255,255))

        self._dem_img_r = pygame.image.load("project\\dementor_r.png")
        self._dem_img_r.set_colorkey((255,255,255))

        self._dem_img_l = pygame.image.load("project\\dementor_l.png")
        self._dem_img_l.set_colorkey((255,255,255))

        self._background = pygame.image.load("project\\backgr.jpg")
        self._highscore= 0
        self._score = 0
        self._shooted_magic = []
        self._potions_in_map = []
        self._dem_on_screen_list = []
        self._vold_on_screen_list = []
        self._num_of_killed_dem = 0
        self.screen = pygame.display.set_mode(WINDOWSIZE)
        self.platforms = [pygame.Rect(0, 710, 1200, 50), pygame.Rect(0, 460, 1200, 50), pygame.Rect(0, 210, 1200, 50)]
        # self.platform_borders = [pygame.Rect(0, 710, 1200, 10), pygame.Rect(0, 460, 1200, 10), pygame.Rect(0, 210, 1200, 10)]
        
    def play(self):

        self.create()
        self._game_over = False
        clock = pygame.time.Clock()
        clock.tick(FPS)

        while self._game_over is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._harry.input_handle()
            self._harry.update()
            
            for dem in self._dem_on_screen_list:
                dem.update()

            for vold in self._vold_on_screen_list:
                vold.update()

            if self._harry.shoot_magic():
                magic = Magic(x=self._harry._position[0]+30,y= self._harry._position[1]+10,direction= self._harry._last_direction)
                def append_to_shooted_magic():
                    self._shooted_magic.append(magic)
                append_to_shooted_magic()
            self.move_magic()
            self.handle_collision()

            def generate_potion(self):
                potion = Potion()
                self._potions_in_map.append(potion)            
            def generate_dem(self):
                dem = Dementor(_last_direction=self._harry._last_direction)
                self._dem_on_screen_list.append(dem)
            
            def generate_vold(self):
                vold = Voldemort(_last_direction=self._harry._last_direction)
                self._vold_on_screen_list.append(vold)
            
            if self.should_generate_dem():
                generate_dem(self)
            if self.should_generate_vold():
                generate_vold(self)
            if self.should_generate_potion():
                generate_potion(self)
            
            self.render()
            if not self._harry.is_alive():
                self._game_over = True
                game_over_screen = GameOverScreen(self._score)
                while self._game_over is True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                self.reset_game()  
                    game_over_screen.render()
                    pygame.display.flip()
            
            self.render()
            clock.tick(FPS)
                

    def render(self):
        def draw_bg():
            self.screen.blit(self._background, (0, 0))
            
        for p in self.platforms:
            pygame.draw.rect(self.screen, WHITE, p)
        # for b in self.platform_borders:
        #     pygame.draw.rect(self.screen, PLATFORM_BORDER_COLOR, b)
        
        def draw_harry():
            self.screen.blit(self._harry._harry_image, self._harry.here_is_pos())

        def draw_potion():
            self.screen.blit(potion.here_is_potion_img(), potion._position)
        
        def draw_dem():
            self.screen.blit(dem.here_is_image(), dem.here_is_pos())
        
        def draw_magic():
            self.screen.blit(magic.here_is_magic_shape(), magic.here_is_pos())
            
        def draw_vold():
            screen.blit(vold.here_is_image(),vold.here_is_pos())

        draw_bg()

        for potion in self._potions_in_map:
            draw_potion()
            
        for dem in self._dem_on_screen_list:
            draw_dem()

        for magic in self._shooted_magic:
            draw_magic()
            
        for vold in self._vold_on_screen_list:
            draw_vold()

        draw_harry()

        self._lifebar.update_bar(self.screen)
        self.show_score()
        pygame.display.flip()

    def create(self):
        self._harry = HarryPotter()
        self._lifebar = LifeBar(self._harry)
        self._voldemort =Voldemort(self._harry._last_direction)
        self._dementor =Dementor(self._harry._last_direction)
        # for height in self._platform_heights:
        #     self._platform = Platform(height)
            
    def reset_game(self):
        if self._score > self._highscore:
            self._highscore=self._score 
        self._score = 0
        self._shooted_magic = []
        self._potions_in_map = []
        self._dem_on_screen_list = []
        self._harry = None
        self._game_over = False
        self.create()

    def handle_collision(self):
        for dem in self._dem_on_screen_list:
            if dem.collides_with(self._harry):
                self._harry.handle_enemy_collision(dem)
        for vold in self._vold_on_screen_list:
            if vold.collides_with(self._harry):
                self._harry.handle_enemy_collision(vold)
        for potion in self._potions_in_map:
            if potion.collides_with(self._harry):
                self._harry.drink_potion()
                potion.is_picked()
                self._potions_in_map.remove(potion)

        for dem in self._dem_on_screen_list:
            for magic in self._shooted_magic:
                if magic.collides_with(dem):
                    self._dem_on_screen_list.remove(dem)
                    self._score += 1  # Increment the score by one point
                    self._shooted_magic.remove(magic)
                    self._num_of_killed_dem += 1

        for vold in self._vold_on_screen_list:
            for magic in self._shooted_magic:
                if magic.collides_with(vold):
                    vold._life -= magic.here_is_magic_damage()
                    if vold.is_alive() == False:
                        self._vold_on_screen_list.remove(vold)
                        self._score += 50 
                    self._shooted_magic.remove(magic)
                    
        self._shooted_magic = [magic for magic in self._shooted_magic if not magic.harry_is_dead()]
        self._dem_on_screen_list = [dem for dem in self._dem_on_screen_list if dem.is_alive()]
        self._vold_on_screen_list = [vold for vold in self._vold_on_screen_list if vold.is_alive()]

    def should_generate_potion(self):
        return random.random() < 0.005
           
    def should_generate_dem(self):
        return len(self._dem_on_screen_list)<15 and random.random() < 0.025
            
    def should_generate_vold(self):
        if len(self._vold_on_screen_list)<1:
            if self._num_of_killed_dem % 20 == 1 and self._num_of_killed_dem>20:
                    return True
        return False
    def show_score(self):
        self._font = pygame.font.Font(None, 30)
        self._score_text = self._font.render(f"Score: {str(self._score)}", True, (255, 255, 255))
        self.screen.blit(self._score_text, (windowwidth-200, 20))
        if self._score>self._highscore:
            self._highscore=self._score
        self._font = pygame.font.Font(None, 30)
        self._score_text = self._font.render(f"Highscore: {str(self._highscore)}", True, (255, 255, 255))
        self.screen.blit(self._score_text, (windowwidth-200, 60))
    def move_magic(self):
        for magic in self._shooted_magic:
            magic.update()
