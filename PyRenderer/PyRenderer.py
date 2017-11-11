import pygame
import numpy
import sys
import math
from Object import Object

pygame.init()
screen = pygame.display.set_mode((1280,720))
cx, cy = 640, 360
pygame.display.set_caption('3D Renderer')
clock = pygame.time.Clock()

# Create an object.
model = Object()
model.test()
model.loadModel("Test Objects/teapot.obj")
print(model.verticies)

while 1:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        print(event)

    screen.fill((255,255,255))

    for x,y,z in model.verticies:
        z+=5
        f = cx/z
        x,y = x*f,y*f
        pygame.draw.circle(screen, (0,0,0),(cx+int(x),cy+int(y)), 1)

    pygame.display.update()