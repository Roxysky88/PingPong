import random
import pygame
import pygame.freetype


def move_player():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def move_AI():
    if ball.centerx > SCREEN_WIDTH/2 and ball_dx > 0:
        if opponent.bottom < ball.top:
            opponent.y += opponent_speed
        elif opponent.top > ball.bottom:
            opponent.y -= opponent_speed


def move_ball(dx, dy):
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        dy = -dy

    if ball.colliderect(player) and dx < 0:
        if abs(ball.left - player.right) < 10:
            dx = -dx
        elif abs(ball.top - player.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(player.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    if ball.colliderect(opponent) and dx > 0:
        if abs(ball.right - opponent.left) < 10:
            dx = -dx
        elif abs(ball.top - opponent.bottom) < 10 and dy < 0:
            dy = -dy
        elif abs(opponent.top - ball.bottom) < 10 and dy > 0:
            dy = -dy

    now = pygame.time.get_ticks()
    if now - score_time > pause_len:
        ball.x += dx
        ball.y += dy

    return dx, dy


def restart_ball(dx, dy):
    ball.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    dx = random.choice((random.randint(-ball_max_speed, -3),
                       random.randint(3, ball_max_speed)))
    dy = random.choice((random.randint(-ball_max_speed, -3),
                       random.randint(3, ball_max_speed)))

    return dx, dy


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

# Colors
BG_COLOR = (50, 50, 50)
PADDLE_COLOR = (20, 20, 20)

# Rectangles
player = pygame.Rect(10, SCREEN_HEIGHT/2, 10, 100)
opponent = pygame.Rect(SCREEN_WIDTH-20, SCREEN_HEIGHT/2, 10, 100)
ball = pygame.Rect(SCREEN_WIDTH/2-10, SCREEN_HEIGHT/2-10, 20, 20)

# Other variables
player_speed = 0
opponent_speed = 7
ball_max_speed = 11
ball_dx, ball_dy = -7, 7

score_time = 0
pause_len = 1000
player_score, opponent_score = 0, 0

# Screen initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
main_font = pygame.freetype.Font(None, 42)

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
    move_AI()
    ball_dx, ball_dy = move_ball(ball_dx, ball_dy)

    if ball.right <= 0:
        opponent_score += 1
    elif ball.left >= SCREEN_WIDTH:
        player_score += 1

    if ball.right <= 0 or ball.left >= SCREEN_WIDTH:
        ball_dx, ball_dy = restart_ball(ball_dx, ball_dy)
        score_time = pygame.time.get_ticks()

    # Draw
    screen.fill(BG_COLOR)
    main_font.render_to(screen, (SCREEN_WIDTH/3, 20), str(player_score))
    main_font.render_to(screen, (SCREEN_WIDTH/1.5, 20), str(opponent_score))

    pygame.draw.rect(screen, PADDLE_COLOR, player)
    pygame.draw.rect(screen, PADDLE_COLOR, opponent)
    pygame.draw.line(screen, PADDLE_COLOR, (SCREEN_WIDTH/2, 0),
                                (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, PADDLE_COLOR, ball)


    clock.tick(60)
    pygame.display.flip()