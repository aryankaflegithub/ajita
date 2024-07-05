import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube(size, color):
    glBegin(GL_LINES)
    glColor3fv(color)
    for edge in edges:
        for vertex in edge:
            glVertex3fv((verticies[vertex][0]*size, verticies[vertex][1]*size, verticies[vertex][2]*size))
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    disks = [
        {"size": 1, "color": (1, 0, 0), "x": 0, "y": 0, "z": 0},
        {"size": 0.8, "color": (0, 1, 0), "x": 0, "y": 0, "z": 0},
        {"size": 0.6, "color": (0, 0, 1), "x": 0, "y": 0, "z": 0}
    ]

    rods = [
        {"x": -2, "y": 0, "z": 0},
        {"x": 0, "y": 0, "z": 0},
        {"x": 2, "y": 0, "z": 0}
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        pygame.display.flip()
        clock.tick(30)    

if __name__ == "__main__":
    main()