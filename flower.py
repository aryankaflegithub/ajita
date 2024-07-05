import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def draw_flower():
    num_petals = 10
    angle_step = 360 / num_petals
    radius = 1.0
    petal_length = 1.5
    petal_width = 0.5

    for i in range(num_petals):
        angle = np.radians(i * angle_step)
        x = np.cos(angle) * radius
        y = np.sin(angle) * radius

        glPushMatrix()
        glTranslatef(x, y, 0)
        glRotatef(np.degrees(angle), 0, 0, 1)
        draw_petal(petal_length, petal_width)
        glPopMatrix()

def draw_petal(length, width):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(length, width / 2, 0.0)
    glVertex3f(length, -width / 2, 0.0)
    glEnd()

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
        
        rotation_angle += 1
        glRotatef(rotation_angle, 0, 0, 1)
        
        draw_flower()
        
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
