import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TD TEST")

running =True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False

    screen.fill((45, 40, 35))
    pygame.display.flip()

pygame.quit()
sys.exit()