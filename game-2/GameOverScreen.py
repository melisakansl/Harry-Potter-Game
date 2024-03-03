Class GameOverScreen:
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
