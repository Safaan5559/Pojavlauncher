import pygame
import random
from settings import ENEMY_SPEED, SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        x = random.randint(0, SCREEN_WIDTH-50)
        self.rect = self.image.get_rect(topleft=(x, -50))

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > 800:
            self.kill()
