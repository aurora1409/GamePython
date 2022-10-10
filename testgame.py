from json import load
import sys
import pygame
import square
pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

sq = square.Square()
sq.GetImage()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(sq.GetImage(), (50, 50))
    pygame.display.update()
    clock.tick(60)
