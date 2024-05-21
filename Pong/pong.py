import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
FPS = 60

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the paddle images
paddle1_image = pygame.image.load('D:/Proyectos personales/juegos pygame/Pong/media_pong/agus.png')
paddle2_image = pygame.image.load('D:/Proyectos personales/juegos pygame/Pong/media_pong/gabi.png')

# Get the size of the images
paddle1_size = paddle1_image.get_size()
paddle2_size = paddle2_image.get_size()

# Set up the ball and paddles
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
paddle1 = pygame.Rect(0, HEIGHT // 2, *paddle1_size)
paddle2 = pygame.Rect(WIDTH - paddle2_size[0], HEIGHT // 2, *paddle2_size)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the ball speed and paddle speed
ball_speed = [2, 2]
paddle_speed = 4

background = pygame.transform.scale(pygame.image.load('D:/Proyectos personales/juegos pygame/Pong/media_pong/fondo.png'), (WIDTH, HEIGHT))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball.move_ip(ball_speed)

    # Move the paddles
    if pygame.key.get_pressed()[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -paddle_speed)
    if pygame.key.get_pressed()[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.move_ip(0, paddle_speed)
    if pygame.key.get_pressed()[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -paddle_speed)
    if pygame.key.get_pressed()[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.move_ip(0, paddle_speed)

    # Collide with edges
    if ball.left < 0 or ball.right > WIDTH:
        pygame.quit()
        sys.exit()

    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1

    # Collide with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *= -1

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(paddle1_image, paddle1.topleft)
    screen.blit(paddle2_image, paddle2.topleft)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)




