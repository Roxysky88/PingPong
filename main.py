import pygame


def move_player():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def move_ball(dx, dy):
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        dy = -dy
    if ball.colliderect(player) or ball.colliderect(opponent):
        dx = -dx
    ball.x += dx
    ball.y += dy

    return dx, dy


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
ball_dx, ball_dy = -7, 7

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
    move_player()
    ball_dx, ball_dy = move_ball(ball_dx, ball_dy)

    # Draw
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, player)
    pygame.draw.rect(screen, PADDLE_COLOR, opponent)
    pygame.draw.line(screen, PADDLE_COLOR, (SCREEN_WIDTH/2, 0),
                                (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, PADDLE_COLOR, ball)


    clock.tick(60)
    pygame.display.flip()


