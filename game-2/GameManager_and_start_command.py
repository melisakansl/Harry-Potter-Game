class GameManager:
    def __init__(self):
        self._game = Game()

    def start(self):
        self._game.play()
game_manager = GameManager()
game_manager.start()
