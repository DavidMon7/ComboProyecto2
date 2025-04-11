import pygame
import random

# Parámetros de obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_velocity = 5
obstacles = []

# Clase para el Obstacle
class Obstacle(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

# Función para crear un nuevo obstáculo
def generate_obstacle():
    x_pos = screen_width
    y_pos = random.randint(100, screen_height - obstacle_height)
    new_obstacle = Obstacle(x_pos, y_pos, obstacle_width, obstacle_height)
    obstacles.append(new_obstacle)

# Función para mover obstáculos
def move_obstacles():
    global obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_velocity
        if obstacle.x < 0:
            obstacles.remove(obstacle)
