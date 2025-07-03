import pygame
from constants import *

class Board:
    def __init__(self):
        pass

    def draw_grid(self, screen):
        for y in range(0, WINDOW_HEIGHT, BOX_SIZE):
            for x in range(0, WINDOW_WIDTH, BOX_SIZE):
                rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
                if (x // BOX_SIZE + y // BOX_SIZE) % 2 == 0:
                    pygame.draw.rect(screen, SPICY_MIX, rect)
                else:
                    pygame.draw.rect(screen, BURLYWOOD, rect)

