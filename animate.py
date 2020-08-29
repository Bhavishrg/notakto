import pygame
import sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600))

def draw_line_animate(surface, color, x1,y1, x2,y2, width):
    x = x1
    y = y1
    val = True
    while val:
        pygame.draw.line(surface, color, (x1,y1),(x,y), width)
        if x != x2:
            x += 0.5
        if y!= y2:
            y += 0.5
        if x == x2 and y == y2:
            val = False
        pygame.display.update()

screen.fill((0,0, 0))
draw_line_animate(screen, (255,255,255), 0,200, 800,200, 20)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
