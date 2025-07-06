import pygame
from settings import Settings

class Mario:

    def __int__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()


        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.bg_color = self.settings.bg_color
        self.rect.center = self.screen_rect.center

    def blitme(self):

        self.screen_blit(self.image, self.rect)