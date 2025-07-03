import pygame

SPICY_MIX = (147, 100, 81)
BURLYWOOD = (221, 179, 140)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

BOX_SIZE = 50

def draw_grid(screen):
    for y in range(0, WINDOW_HEIGHT, BOX_SIZE):
        for x in range(0, WINDOW_WIDTH, BOX_SIZE):
            rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
            if (x // BOX_SIZE + y // BOX_SIZE) % 2 == 0:
                pygame.draw.rect(screen, SPICY_MIX, rect)
            else:
                pygame.draw.rect(screen, BURLYWOOD, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()

        screen.fill((0,0,0))
        draw_grid(screen)
        pygame.display.flip()





if __name__ == "__main__":
    main()

