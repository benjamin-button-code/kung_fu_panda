import pygame
pygame.init()


# Images
path_to_images = r"./images/"
icon_image = pygame.image.load(path_to_images + r"kung_fu_panda_icon.jpg")

# Window/Screen
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_icon(icon_image)
pygame.display.set_caption("Kung fu panda")

# Some constants
FPS = 60
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FLOOR = HEIGHT // 2 + 100
x, y = 0, FLOOR
speed_move = 5
height_jump = FLOOR - 70
speed_jump = 3

JUMPING = False
GAME_LOOP = True

# Main loop
while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GAME_LOOP = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y == FLOOR:
                JUMPING = True
        elif event.type == pygame.KEYUP:
            pass

    # Move(right or left)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < WIDTH - 20:
        x += speed_move
    elif keys[pygame.K_LEFT] and x > 0:
        x -= speed_move

    # Jumping
    if JUMPING and y >= height_jump:
        y -= speed_jump
    elif y == FLOOR:
        JUMPING = False
    elif y <= FLOOR:
        y += speed_jump
        JUMPING = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x, y, 20, 50))
    pygame.display.update()

    clock.tick(FPS)

