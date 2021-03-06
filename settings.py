import pygame

vector = pygame.math.Vector2
WIN_WIDTH = 700
WIN_HEIGHT = 350
ACCELERATION = 0.4
FRICTION = -0.1
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
GAME_LOOP = True
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
one_frame_time = 5


# Load images
def load_convert(path_to_folder, lst, frames=one_frame_time):
    images = []
    for name in lst:
        path = f"Images/{path_to_folder}/{name}"
        for i in range(frames):
            images.append(pygame.image.load(path).convert_alpha())
    return images


icon = pygame.image.load("Images/kung_fu_panda_icon.jpg")
background_image = pygame.image.load("Images/Background/Background.png").convert_alpha()
ground_image = pygame.image.load("Images/Background/Ground.png").convert_alpha()

# Stay animation
stay_animation_R = ['Player_stay_R _1.png', 'Player_stay_R _2.png',
                    'Player_stay_R _3.png', 'Player_stay_R _4.png']

# Attack animation for the RIGHT
attack_animation_R = []

# Attack animation for the LEFT
attack_animation_L = []

# Run animation for the RIGHT
run_ani_R = []

# Run animation for the LEFT
run_ani_L = []

max_attack_frame = (len(attack_animation_R) - 1) * one_frame_time
max_move_frame = (len(run_ani_R) - 1) * one_frame_time
max_stay_frame = (len(stay_animation_R) - 1) * 14

stay_animation_R = load_convert("Stay_Animations", stay_animation_R, 14)
stay_animation_L = [pygame.transform.flip(image, 1, 0) for image in stay_animation_R]

attack_animation_R = load_convert("Attack_Animations", attack_animation_R)
attack_animation_L = load_convert("Attack_Animations", attack_animation_L)

run_ani_R = load_convert("Movement_Animations", run_ani_R)
run_ani_L = load_convert("Movement_Animations", run_ani_L)
