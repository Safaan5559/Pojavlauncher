import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
from coin import Coin

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Collector")
clock = pygame.time.Clock()

player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT-100)
player_group = pygame.sprite.Group()
player_group.add(player)

enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

score = 0
frame_count = 0
running = True

while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    frame_count += 1
    if frame_count % SPAWN_ENEMY_RATE == 0:
        enemy_group.add(Enemy())
    if frame_count % SPAWN_COIN_RATE == 0:
        coin_group.add(Coin())

    player_group.update(keys)
    enemy_group.update()
    coin_group.update()

    if pygame.sprite.spritecollide(player, enemy_group, False):
        running = False
    collected = pygame.sprite.spritecollide(player, coin_group, True)
    score += len(collected)

    screen.fill((0, 0, 50))
    player_group.draw(screen)
    enemy_group.draw(screen)
    coin_group.draw(screen)

    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10, 10))

    pygame.display.flip()

pygame.quit()
print("Game Over! Score:", score)
