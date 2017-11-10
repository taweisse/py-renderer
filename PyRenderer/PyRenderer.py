import pygame
import sys
import math
from Object import Object

pygame.init()

# The resolution of the output window.
resX, resY = 1280, 720
screen = pygame.display.set_mode((resX, resY))

# Find the middle of the output window.
cx = int(resX/2)
cy = int(resY/2)

pygame.display.set_caption('3D Renderer')
clock = pygame.time.Clock()

# Create an object.
model = Object()
model.test()
model.loadModel("teapot.obj")
print(model.verticies)

# Flag to tell if the user is clicking and dragging.
# If they are, we need to rotate the model accordingly.
mouseDrag = False;

while 1:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDrag = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDrag = False
            
        print(event)
        print(mouseDrag)

    screen.fill((255,255,255))

    for x,y,z in model.verticies:
        z+=5
        f = cy/z
        x,y = x*f,y*f
        pygame.draw.circle(screen, (0,0,0),(cx-int(x),cy-int(y)), 1)

    pygame.display.update()