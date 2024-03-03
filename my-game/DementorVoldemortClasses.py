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
