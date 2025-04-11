import pygame
import random

# Inicialización de fuentes de sonidos
pygame.mixer.init()

# Sonidos
jump_sound = pygame.mixer.Sound("assets/jump.wav")
coin_sound = pygame.mixer.Sound("assets/coin_collect.wav")
game_over_sound = pygame.mixer.Sound("assets/game_over.wav")

# Función para reproducir sonido de salto
def play_jump_sound():
    jump_sound.play()

# Función para reproducir sonido de coin
def play_coin_sound():
    coin_sound.play()

# Función para reproducir sonido de game over
def play_game_over_sound():
    game_over_sound.play()

# Fondo de pantalla
def load_background():
    return pygame.image.load("assets/background.png")

