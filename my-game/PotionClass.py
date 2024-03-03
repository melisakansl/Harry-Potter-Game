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
