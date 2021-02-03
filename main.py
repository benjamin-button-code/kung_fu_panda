import classes
from settings import *
import sys
import random
import tkinter as tk
from tkinter import filedialog
import pygame

pygame.init()
pygame.display.set_caption('Kung Fu Panda')
pygame.display.set_icon(icon)

# Objects
background = classes.Background(background_image)
ground = classes.Ground(ground_image)
ground_group = pygame.sprite.Group()
ground_group.add(ground)
player = classes.Player()

while GAME_LOOP:
    player.gravity_check(ground_group)
    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == pygame.QUIT:
            GAME_LOOP = False
            sys.exit()
        # For event that occur upon mouse clicking
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        # Event handling for a range of different key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.jump(ground_group)

    # Actions
    player.update()
    player.move()
    # Draw
    background.render()
    ground.render()
    player.update()
    display_surface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
