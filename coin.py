import pygame
import random
from settings import COIN_SPEED, SCREEN_WIDTH

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 0))
        x = random.randint(0, SCREEN_WIDTH-30)
        self.rect = self.image.get_rect(topleft=(x, -30))

    def update(self):
        self.rect.y += COIN_SPEED
        if self.rect.top > 800:
            self.kill()
