from settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.background_image = image
        self.bg_x = 0
        self.bg_y = 0

    def render(self):
        display_surface.blit(self.background_image, (self.bg_x, self.bg_y))


class Ground(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self):
        display_surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = stay_animation_R[0]
        self.rect = self.image.get_rect(center=(240, 255))

        # Movement
        self.is_stay = True
        self.is_jumping = False
        self.is_running = False
        self.stay_frame = 0
        self.move_frame = 0

        # Position
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)
        self.pos = vector((100, 240))
        self.direction = "RIGHT"

    def move(self):
        self.acc = vector(0, 0)
        if abs(self.vel.x) >= 0.5:
            self.is_running = True
            self.is_stay = False
        else:
            self.is_running = False
            self.is_stay = True

        pressed_keys = pygame.key.get_pressed()
        # Acceleration according direction
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACCELERATION
        elif pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACCELERATION

        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates position with new values

        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        elif self.pos.x > WIN_WIDTH:
            self.pos.x = 0

        self.rect.midbottom = self.pos

    def update(self):
        # Returns direction
        if self.vel.x > 0:
            self.direction = "RIGHT"
        elif self.vel.x < 0:
            self.direction = "LEFT"

        # Animation stay frames according direction
        if self.is_stay:
            if self.stay_frame > max_stay_frame:
                self.stay_frame = 0
                return
            if self.direction == "RIGHT":
                self.image = stay_animation_R[self.stay_frame]
            elif self.direction == "LEFT":
                self.image = stay_animation_L[self.stay_frame]
            self.stay_frame += 1

        # Animation running frames according direction
        if self.is_running:
            if self.move_frame > max_move_frame:
                self.move_frame = 0
                return
            if self.direction == "RIGHT":
                self.image = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L[self.move_frame]
            self.move_frame += 1

    def punch(self):
        pass

    def kick(self):
        pass

    def jump(self):
        pass

    def gravity_check(self):
        pass


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
