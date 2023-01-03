import pygame


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

# Colors
BG_COLOR = (50, 50, 50)
PADDLE_COLOR = (20, 20, 20)

# Rectangles
player = pygame.Rect(10, SCREEN_HEIGHT/2, 10, 100)
opponent = pygame.Rect(SCREEN_WIDTH-20, SCREEN_HEIGHT/2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20, 20)

# Other variables
player_speed = 0

# Screen initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 7
            elif event.key == pygame.K_s:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            elif event.key == pygame.K_s:
                player_speed -= 7

    # Update
    player.y += player_speed

    # Draw
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, player)

    clock.tick(60)
    pygame.display.flip()