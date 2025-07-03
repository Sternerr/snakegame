import pygame
from constants import *

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self._body = [(400, 400), (400, 450), (450, 500)]
        self._direction = (0, 0)

    def draw(self, screen):
        for cell in self._body:
            rect = pygame.Rect(*cell, BOX_SIZE, BOX_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect) 

    def move(self):
        head_x, head_y = self._body[0]
        new_head = (head_x + self._direction[0], head_y + self._direction[1])
        self._body.pop()
        self._body.insert(0, new_head)
    
    def direction(self, direction):
        
        opposite = (-self._direction[0], -self._direction[1])
        if opposite != direction:
            self._direction = direction

    def is_out_of_bounds(self):
        head_x, head_y = self._body[0]
        return (
            head_x < 0
            or head_x > WINDOW_WIDTH
            or head_y < 0
            or head_y > WINDOW_HEIGHT
        )

