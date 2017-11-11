import pygame
import sys
import math
import numpy
import operator
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
mousePrePos = (-1,-1)
mouseCurPos = (-1,-1)

while 1:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Set the mouseDrag flag if the user clicks the mouse.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDrag = True
            
        # Unset the mouseDrag flag when the user lets the button up.
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDrag = False
                mouseCurPos = (-1,-1)

        # Record the location of the mouse if the user is dragging.
        if (event.type == pygame.MOUSEMOTION and mouseDrag):
            mousePrePos = mouseCurPos
            mouseCurPos = event.pos
            
        print(event)

    # Rotate the model based on the current and previous mouse coords.
    if (mouseDrag and mousePrePos != (-1,-1)):
        mouseMov = tuple(map(operator.sub, mouseCurPos, mousePrePos))
        print(mouseMov)

    # Fill the screen with white as a background.
    screen.fill((255,255,255))

    for x,y,z in model.verticies:
        z+=5
        f = cy/z
        x,y = x*f,y*f
        pygame.draw.circle(screen, (0,0,0),(cx-int(x),cy-int(y)), 1)

    pygame.display.update()