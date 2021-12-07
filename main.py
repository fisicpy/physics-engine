# import modules
import pygame
import object.ball

pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Program")
clock = pygame.time.Clock()

ball = object.ball.Ball(screen)


if __name__ == "__main__":
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        screen.fill((255, 255, 255))

        ball.draw()

        pygame.display.flip()
        clock.tick(30)
