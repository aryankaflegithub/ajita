import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def draw_blade(length, width):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)  # White color for the blades
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(length, width / 2, 0.0)
    glVertex3f(length, -width / 2, 0.0)
    glEnd()

def draw_windmill(num_blades, length, width):
    angle_step = 360 / num_blades
    for i in range(num_blades):
        glPushMatrix()
        glRotatef(i * angle_step, 0, 0, 1)
        draw_blade(length, width)
        glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    clock = pygame.time.Clock()
    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glRotatef(rotation_angle, 0, 0, 1)
        draw_windmill(4, 2.0, 0.5)  # Draw windmill with 4 blades
        glPopMatrix()

        pygame.display.flip()
        rotation_angle += 1  # Rotate blades
        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
