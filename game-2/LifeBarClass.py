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
