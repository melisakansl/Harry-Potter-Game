import pygame, sys, random
import time

WINDOWSIZE = windowwidth, windowheight = 1200, 760
PLATFORM_BORDER_COLOR = (128, 139, 140)
TEXT_COLOR = (33, 88, 105)
WHITE = (255, 255, 255)
FPS=60
pygame.init()

screen = pygame.display.set_mode(WINDOWSIZE)


class Entity:
    def __init__(self, _last_direction = "right"):
        self._position = [0, 0]
        self._last_direction = "right"

    def collides_with(self, other_entity):
        return pygame.Rect(self._position[0], self._position[1], 32, 32).colliderect(
            pygame.Rect(other_entity.here_is_pos()[0], other_entity.here_is_pos()[1], 32, 32))
    def here_is_pos(self):
        return self._position
    def is_alive(self):
        return self._life>0

class Enemy(Entity):
    def __init__(self, _last_direction = "right", _is_voldemort = "False", _position = [0,0]):
        super().__init__(_last_direction)
        self._position = [random.randint(1, 10) * 100, 650 - random.randint(0, 4) * 150]
        self._is_voldemort = False
    def here_is_harry_position(self):
        return game_manager._game._harry.here_is_pos()
    def here_is_damage(self):
        return self._damage
    def here_is_image(self):
        return self._image
    def is_alive(self):
        return self._life > 0
    def update(self):
        player_position = self.here_is_harry_position()  
        enemy_position = self.here_is_pos()

        def update_to_left(self):
            enemy_position[0] -= 2 
            self._image = self._image_left 
        def update_to_right(self):
            enemy_position[0] += 2 
            self._image = self._image_right 

        if player_position[0] < enemy_position[0]:
            update_to_left(self)
        else:
            update_to_right(self)

        self._position = enemy_position
    def handle_magic_collision(self, magic):
        self._life -= magic.here_is_magic_damage()

class Dementor(Enemy):
    def __init__(self, _last_direction=None, _is_voldemort = None, _position = None):
        super().__init__(_last_direction,_is_voldemort, _position)
        self._life = 2
        self._image = pygame.image.load("project\\dementor_r.png")
        self._image_right = pygame.image.load("project\\dementor_r.png")
        self._image_left = pygame.image.load("project\\dementor_l.png")
        self._damage = 25

        
class Voldemort(Enemy):
    def __init__(self, _last_direction=None, _is_voldemort = None, _position = None):
        super().__init__(_last_direction,_is_voldemort, _position)
        self._life = 1000
        self._image = pygame.image.load("project\\voldemort_r.png")
        self._image.set_colorkey((255, 255, 255))

        self._image_right = pygame.image.load("project\\voldemort_r.png")
        self._image_right.set_colorkey((255, 255, 255))

        self._image_left = pygame.image.load("project\\voldemort_l.png")
        self._image_left.set_colorkey((255,255,255))

        self._damage = 34



class Magic(Entity):
    def __init__(self, x, y, direction):
        super().__init__()
        self._position = [x, y]
        self._image = pygame.image.load("project\\magic_l.png")
        self._image.set_colorkey((255,255,255))
        self._magic_direction = direction
        self._magic_speed = 10
        self._magic_damage = 334
    def update(self):
        if self._magic_direction == "right":
            self.magic_turn_right()
        elif self._magic_direction == "left":
            self.magic_turn_left()
    def magic_turn_right(self):
        self._position[0] += self._magic_speed
    def magic_turn_left(self):
        self._position[0] -= self._magic_speed
    def here_is_magic_damage(self):
        return self._magic_damage
    def harry_is_dead(self):
        return False
    def here_is_magic_shape(self):
        return self._image
    def magic_reached_enemy(self, enemy):
        return super().collides_with(enemy)
    def here_is_damage(self):
        return self._magic_damage
            

class HarryPotter(Entity):
    def __init__(self):
        super().__init__()
        self._position = [0,650]
        self._life = 100
        self._harry_image = pygame.image.load("project\\harry_r.png")
        self._harry_image.set_colorkey((255,255,255))
        self._jump_height = 145
        self._jump_speed = 7
        self._fall_speed = 7
        self._jump_start_pos = 0
        self._fall_start_pos = 0
        self._is_jumping = False
        self._is_falling = False
        self._jump_cooldown = 600
        self._magic_cooldown = 600
        self._last_jump_time = 0
        self._last_magic_shoot_time = 0
        self._last_damage_time = 0
        self._invincibility_cooldown = 600

    def shoot_magic(self):
        if self._keys[pygame.K_SPACE] and pygame.time.get_ticks()-self._last_magic_shoot_time>self._magic_cooldown:
            self._last_magic_shoot_time=pygame.time.get_ticks()
            return True
        else:
            return False
    def is_alive(self):
        return self._life > 0
    def drink_potion(self):
        if self._life<=50:
            self._life+=50
        else:
            self._life=100
    def here_is_harry_life(self):
        return self._life
    def draw(self, path):
        self._harry_image=pygame.image.load(path)
        self._harry_image.set_colorkey((255,255,255))
    def update(self):
        if pygame.time.get_ticks()>1:
            if self._last_direction=="left":
                self.draw("project\\harry_l.png")
            else:
                self.draw("project\\harry_r.png")
    def handle_enemy_collision(self, enemy):
        if pygame.time.get_ticks() - self._last_damage_time > self._invincibility_cooldown:
            self._life -= enemy.here_is_damage()
            self._last_damage_time=pygame.time.get_ticks()
    def here_is_max_life(self):
        return 100
    def should_shoot_magic(self):
        self._keys = pygame.key.get_pressed()
        return self._keys[pygame.K_SPACE]
    def input_handle(self):
        def move_left():
            self._position[0] -= 5
            self._last_direction = "left"
        def move_right():
            self._position[0] += 5
            self._last_direction = "right"
        def jump_up():
            self._jump_start_pos = self._position[1]
            self._last_jump_time = current_time
        def jump_down():
            self._fall_start_pos = self._position[1]
        
        self._keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if not self._is_jumping and not self._is_falling:
            if self._keys[pygame.K_UP] and current_time - self._last_jump_time >= self._jump_cooldown and self._position[1]>100:
                self._is_jumping = True
                jump_up()   
            elif self._keys[pygame.K_DOWN] and current_time - self._last_jump_time >= self._jump_cooldown and self._position[1]<600:
                self._is_falling = True
                jump_down()
                
        if self._is_jumping:
            if self._position[1] > self._jump_start_pos - self._jump_height:
                self._position[1] -= self._jump_speed
            else:
                self._is_jumping = False

        if self._is_falling:
            if self._position[1] < self._fall_start_pos + self._jump_height:
                self._position[1] += self._jump_speed
            else:
                self._is_falling = False

        if self._keys[pygame.K_LEFT] and self._position[0]>0:
            move_left()
            
        if self._keys[pygame.K_RIGHT] and self._position[0]<1150:
            move_right()
class LifeBar:
    def __init__(self, harry):
        self._harry = harry
        self._position = [10,10]
        self._width = 200
        self._height = 20
        self._initial_life = harry.here_is_max_life()
    def update_bar(self,screen):
        health_percentage = self._harry.here_is_harry_life() / self._initial_life
        fill_width = int(self._width * health_percentage)

        pygame.draw.rect(screen, WHITE, (self._position[0], self._position[1], self._width, self._height), 2)

        pygame.draw.rect(screen, (255, 0, 0), (self._position[0], self._position[1], fill_width, self._height))
        self._font = pygame.font.Font(None, 20)
        self._score_text = self._font.render(f"Health: {str(self._harry.here_is_harry_life())}", True, (255, 255, 255))
        screen.blit(self._score_text, (self._position[0]+10,self._position[1]+5))

class Potion(Entity):
    def __init__(self):
        self._potion_image = pygame.image.load("project\\potion_s.png")
        self._potion_image.set_colorkey((255,255,255))
        self._position = [random.randint(1, 10) * 100, 680 - random.randint(0, 4) * 150]
        self._is_picked = False
    def is_picked(self):
        return self._is_picked
    def here_is_potion_img(self):
        return self._potion_image

        
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

class GameOverScreen:
    def __init__(self, score):
        self._score = score
        self._font = pygame.font.Font(None, 50)
        self._text_color = WHITE
        self._game_over_text = self._font.render("Game Over", True, self._text_color)
        self._score_text = self._font.render(f"Score: {self._score}", True, self._text_color)
        self._play_again_text = self._font.render("Press SPACE to play again", True, self._text_color)
        self.screen = pygame.display.set_mode(WINDOWSIZE)


    def render(self):
        self.screen.blit(self._game_over_text, (windowwidth // 2 - self._game_over_text.get_width() // 2, 200))
        self.screen.blit(self._score_text, (windowwidth // 2 - self._score_text.get_width() // 2, 300))
        self.screen.blit(self._play_again_text, (windowwidth // 2 - self._play_again_text.get_width() // 2, 400))
        pygame.display.flip()

    def handle_input(self):
        self._keys = pygame.key.get_pressed()
        if self._keys[pygame.K_SPACE]:
            game_manager._game.reset_game()
            return True
        return False

class GameManager:
    def __init__(self):
        self._game = Game()

    def start(self):
        self._game.play()
game_manager = GameManager()
game_manager.start()
