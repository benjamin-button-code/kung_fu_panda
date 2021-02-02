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

while GAME_LOOP:
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
            pass

    # Draw
    background.render()
    ground.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
