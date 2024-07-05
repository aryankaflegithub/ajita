import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Windmill:
    def __init__(self):
        self.angle = 0
        self.speed = 1

    def draw_hub(self):
        glBegin(GL_QUADS)
        glVertex3fv((-0.2, -0.2, 0.0))
        glVertex3fv((0.2, -0.2, 0.0))
        glVertex3fv((0.2, 0.2, 0.0))
        glVertex3fv((-0.2, 0.2, 0.0))
        glEnd()

    def draw_blades(self):
        glBegin(GL_TRIANGLES)
        glVertex3fv((-0.5, -0.5, 0.0))
        glVertex3fv((0.5, -0.5, 0.0))
        glVertex3fv((0.0, 0.5, 0.0))
        glEnd()

    def draw_tower(self):
        glBegin(GL_QUADS)
        glVertex3fv((-0.1, -0.1, 0.0))
        glVertex3fv((0.1, -0.1, 0.0))
        glVertex3fv((0.1, 0.1, 0.0))
        glVertex3fv((-0.1, 0.1, 0.0))
        glEnd()

    def draw(self):
        glPushMatrix()
        glTranslatef(0.0, 0.0, -2.0)
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        self.draw_hub()
        self.draw_blades()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.0, 0.0, -1.5)
        self.draw_tower()
        glPopMatrix()

    def update(self):
        self.angle += self.speed
        if self.angle > 360:
            self.angle -= 360

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    windmill = Windmill()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        windmill.draw()
        windmill.update()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()