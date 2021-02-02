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

    def move(self):
        pass

    def update(self):
        pass

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
