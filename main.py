import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()

        screen.fill((0, 0, 0))
        pygame.display.flip()





if __name__ == "__main__":
    main()

