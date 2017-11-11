import pygame
import sys
import math
import numpy
import operator
import RenderSettings
from Object import Object

pygame.init()

# The resolution of the output window.
resX, resY = RenderSettings.resolution[0], RenderSettings.resolution[1]
screen = pygame.display.set_mode((resX, resY))

# Find the middle of the output window.
cx = int(resX/2)
cy = int(resY/2)

pygame.display.set_caption('3D Renderer')
clock = pygame.time.Clock()

# Create an object.
model = Object()
model.loadModel("teapot.obj")
print(model.verticies)

# Flag to tell if the user is clicking and dragging.
# If they are, we need to rotate the model accordingly.
mouseOrbit = False
mouseMove = False

while 1:
    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Set the mouseOrbit flag if the user clicks the mouse.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mouse.get_rel()
                mouseOrbit = True
            if event.button == 2:
                pygame.mouse.get_rel()
                mouseMove = True
            
        # Unset the mouseMove flag when the user lets the button up.
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseOrbit = False
            if event.button == 2:
                mouseMove = False
            
        print(event)

    # Rotate the model based on the current and previous mouse coords.
    if mouseOrbit:
        # Determine how far the mouse moved since last frame.
        change = pygame.mouse.get_rel()
        print(change)

    if mouseMove:
        change = pygame.mouse.get_rel()
        print(change)

        # Change the coords of each vertex in the list.
        for i in range(0,len(model.verticies)):
            model.verticies[i][0] -= change[0] * RenderSettings.moveSpeed
            model.verticies[i][1] -= change[1] * RenderSettings.moveSpeed

    # Fill the screen with white as a background.
    screen.fill((255,255,255))

    for x,y,z,ex in model.verticies:
        z+=5
        f = cy/z
        x,y = x*f,y*f
        pygame.draw.circle(screen, (0,0,0),(cx-int(x),cy-int(y)), 1)

    pygame.display.update()