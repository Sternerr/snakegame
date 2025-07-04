import pygame
import random

from constants import *

class Food:
    def __init__(self):
        self._position = self._generate_position()

    def get_position(self):
        return self._position

    def _generate_position(self):
        return (
           random.randrange(0, WINDOW_WIDTH, BOX_SIZE),
           random.randrange(0, WINDOW_HEIGHT, BOX_SIZE)
        )

    def draw(self, screen):
        rect = pygame.Rect(self._position[0], self._position[1], BOX_SIZE, BOX_SIZE)
        pygame.draw.rect(screen, CHOCOLATE_COSMOS, rect) 

