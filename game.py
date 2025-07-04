import pygame

from constants import *
from snake import Snake
from board import Board
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()
        self._board = Board()
        self._snake = Snake()
        self._food = Food()
        self._running = False
        self._direction_changed = False

    def start(self):
        last_move_time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                if event.type == pygame.KEYDOWN and not self._direction_changed:
                    if event.key == pygame.K_UP:
                        self._snake.direction((0, -BOX_SIZE))
                        self._running = True
                        self._direction_changed = True
                    elif event.key == pygame.K_DOWN:
                        self._snake.direction((0, BOX_SIZE))
                        self._running = True
                        self._direction_changed = True
                    elif event.key == pygame.K_LEFT:
                        self._snake.direction((-BOX_SIZE, 0))
                        self._running = True
                        self._direction_changed = True
                    elif event.key == pygame.K_RIGHT:
                        self._snake.direction((BOX_SIZE, 0))
                        self._running = True
                        self._direction_changed = True

        
            current_time = pygame.time.get_ticks()

            if self._running:
                if current_time - last_move_time >= MOVE_INTERVAL:
                    self._snake.move()
                    last_move_time = current_time
                    self._direction_changed = False
               
            if self._snake.is_out_of_bounds() or self._snake.has_collided_with_itself():
                self._reset()
            
            if self._snake.get_head() == self._food.get_position():
                self._snake.grow()
                self._food = Food()

            self._draw()

            self._clock.tick(60)

    def _reset(self):
        self._snake = Snake()
        self._food = Food()

    def _draw(self):
        self._screen.fill((0,0,0))
        self._board.draw_grid(self._screen)

        self._snake.draw(self._screen)
        self._food.draw(self._screen)
        pygame.display.flip()
