import pygame
from constants import *
from snake import Snake
from board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    last_move_time = pygame.time.get_ticks()
    

    board = Board()
    snake = Snake()

    while True:
        if snake.is_out_of_bounds():
            pygame.QUIT()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction((0, -BOX_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.direction((0, BOX_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.direction((-BOX_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.direction((BOX_SIZE, 0))

        screen.fill((0,0,0))
        board.draw_grid(screen)

        snake.draw(screen)
    
        current_time = pygame.time.get_ticks()
        if current_time - last_move_time >= MOVE_INTERVAL:
            snake.move()
            last_move_time = current_time
        
        pygame.display.flip()

        clock.tick(60)





if __name__ == "__main__":
    main()

