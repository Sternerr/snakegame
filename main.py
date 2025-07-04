import pygame
import random

from constants import *
from snake import Snake
from board import Board

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



class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()
        self._board = Board()
        self._snake = Snake()
        self._food = Food()
        self._running = True

    def start(self):
        last_move_time = pygame.time.get_ticks()
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self._snake.direction((0, -BOX_SIZE))
                    elif event.key == pygame.K_DOWN:
                        self._snake.direction((0, BOX_SIZE))
                    elif event.key == pygame.K_LEFT:
                        self._snake.direction((-BOX_SIZE, 0))
                    elif event.key == pygame.K_RIGHT:
                        self._snake.direction((BOX_SIZE, 0))

            self._screen.fill((0,0,0))
            self._board.draw_grid(self._screen)

            self._snake.draw(self._screen)
            self._food.draw(self._screen)
        
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time >= MOVE_INTERVAL:
                self._snake.move()
                last_move_time = current_time
           
            if self._snake.is_out_of_bounds():
                self._reset()
            
            if self._snake.get_head() == self._food.get_position():
                self._snake.grow()
                self._food = Food()

            pygame.display.flip()

            self._clock.tick(60)

    def _reset(self):
        self._snake = Snake()
        self._food = Food()



def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
