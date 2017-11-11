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

# Set up the world coords.
worldPos = [0,0,0]

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

    # Rotate the model based on the current and previous mouse coords.
    if mouseOrbit:
        # Determine how far the mouse moved since last frame.
        change = pygame.mouse.get_rel()
        sinX = math.sin(math.radians(change[0]))
        cosX = math.cos(math.radians(change[0]))
        
        # Rotate each point based on mouse movement.
        for i in range(0, len(model.verticies)):

            # Move point to be relative to the origin.
            xTmp = model.verticies[i][0] #- model.worldPos[0]
            yTmp = model.verticies[i][2] #- model.worldPos[2]

            # Rotate about y.
            xNew = xTmp*cosX - yTmp*sinX
            yNew = xTmp*sinX + yTmp*cosX

            model.verticies[i][0] = xNew #+ model.worldPos[0]
            model.verticies[i][2] = yNew #+ model.worldPos[2]

    if mouseMove:
        change = pygame.mouse.get_rel()

        # Change the coords of each vertex in the list.
        for i in range(0,len(model.verticies)):
            model.verticies[i][0] -= change[0] * RenderSettings.moveSpeed
            model.verticies[i][1] -= change[1] * RenderSettings.moveSpeed

            # Update model's world position.
            model.worldPos[0] -= change[0] * RenderSettings.moveSpeed
            model.worldPos[1] -= change[1] * RenderSettings.moveSpeed

    # Fill the screen with white as a background.
    screen.fill((255,255,255))

    #for x, y, z, ex in model.verticies:
    #    z += 5
    #    f = cy / z
    #    x, y = x * f, y * f
    #    pygame.draw.circle(screen, (0, 0, 0),(cx - int(x), cy - int(y)), 1)

    for edge in model.edges:

        points = list()

        for x, y, z, ex in (model.verticies[edge[0]], model.verticies[edge[1]]):
            z += 5
            f = cy / z
            x, y = x * f, y * f
            points += [(cx - int(x), cy - int(y))]

        pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 1)

    pygame.display.update()