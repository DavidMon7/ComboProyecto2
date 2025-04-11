import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combodruado")

# FPS
clock = pygame.time.Clock()

# Jugador
player_size = 50
player_x = 100
player_y = screen_height - player_size - 10
player_velocity = 5
jumping = False
jump_count = 10

# Obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_velocity = 5
obstacles = []

# Monedas
coin_radius = 20
coins = []

# Función para dibujar el jugador
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

# Función para dibujar obstáculos
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)

# Función para dibujar monedas
def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, (255, 223, 0), (coin[0], coin[1]), coin_radius)

# Función principal del juego
def game():
    global player_y, jumping, jump_count, player_x

    run = True
    while run:
        screen.fill(WHITE)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()

        # Movimiento del jugador
        if keys[pygame.K_LEFT]:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT]:
            player_x += player_velocity

        # Salto
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_y -= (jump_count ** 2) * 0.4 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 10

        # Dibujar jugador, obstáculos y monedas
        draw_player(player_x, player_y)
        draw_obstacles()
        draw_coins()

        # Generar obstáculos
        if random.randint(1, 60) == 1:
            obstacles.append(pygame.Rect(screen_width, screen_height - obstacle_height - 10, obstacle_width, obstacle_height))

        # Mover obstáculos
        for obstacle in obstacles:
            obstacle.x -= obstacle_velocity
            if obstacle.x < 0:
                obstacles.remove(obstacle)

        # Mover monedas
        for coin in coins:
            coin[0] -= 5
            if coin[0] < 0:
                coins.remove(coin)

        # Actualizar pantalla
        pygame.display.update()
        clock.tick(30)

# Ejecutar juego
game()

pygame.quit()

# Variables de juego
score = 0
combo = 0
coins_collected = 0
ranking = []

# Función para actualizar el puntaje
def update_score():
    global score
    score += 10

# Función para generar monedas con efectos
def generate_coin():
    if random.randint(1, 50) == 1:  # Chance de generar moneda
        x_pos = screen_width
        y_pos = random.randint(100, screen_height - 100)
        coins.append([x_pos, y_pos])

# Función para comprobar si el jugador recogió una moneda
def check_coin_collision():
    global combo, coins_collected
    for coin in coins:
        coin_rect = pygame.Rect(coin[0] - coin_radius, coin[1] - coin_radius, coin_radius*2, coin_radius*2)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if coin_rect.colliderect(player_rect):
            coins.remove(coin)
            coins_collected += 1
            update_score()
            combo += 1
            if combo >= 3:
                # Efecto de combo, puedes agregar más cosas aquí
                print("Combo activo!")
            break

# Función para guardar el ranking
def save_ranking():
    global ranking
    name = input("Ingresa tu nombre: ")
    email = input("Ingresa tu correo: ")
    ranking.append((name, email, score))
    ranking.sort(key=lambda x: x[2], reverse=True)
    
    with open("ranking.txt", "w") as file:
        for entry in ranking:
            file.write(f"{entry[0]} - {entry[1]} - {entry[2]}\n")

# Función principal del juego
def game():
    global player_y, jumping, jump_count, player_x, combo, coins_collected

    run = True
    while run:
        screen.fill(WHITE)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_ranking()  # Guardar el ranking al cerrar el juego
                run = False
        
        keys = pygame.key.get_pressed()

        # Movimiento del jugador
        if keys[pygame.K_LEFT]:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT]:
            player_x += player_velocity

        # Salto
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_y -= (jump_count ** 2) * 0.4 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 10

        # Generación de monedas y obstáculos
        generate_coin()
        check_coin_collision()

        # Dibujar jugador, obstáculos y monedas
        draw_player(player_x, player_y)
        draw_obstacles()
        draw_coins()

        # Mover obstáculos
        for obstacle in obstacles:
            obstacle.x -= obstacle_velocity
            if obstacle.x < 0:
                obstacles.remove(obstacle)

        # Mover monedas
        for coin in coins:
            coin[0] -= 5
            if coin[0] < 0:
                coins.remove(coin)

        # Mostrar puntaje
        font = pygame.font.SysFont(None, 55)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Mostrar combo
        combo_text = font.render(f"Combo: {combo}", True, (0, 0, 0))
        screen.blit(combo_text, (10, 60))

        # Actualizar pantalla
        pygame.display.update()
        clock.tick(30)

# Ejecutar juego
game()

pygame.quit()
