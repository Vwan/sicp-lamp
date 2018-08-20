import pygame
from pygame.locals import *
from sys import exit

help(pygame.display)

def main():
    pygame.init()

    img = pygame.image.load("test.png")
    pygame.display.set_icon(img)
    pygame.display.set_caption("hello")

    screen = pygame.display.set_mode((240,180))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()