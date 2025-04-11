import pygame

# Cargar imágenes de assets
def load_images():
    player_image = pygame.image.load("assets/player.png")
    obstacle_image = pygame.image.load("assets/obstacle.png")
    coin_image = pygame.image.load("assets/coin.png")
    return player_image, obstacle_image, coin_image
