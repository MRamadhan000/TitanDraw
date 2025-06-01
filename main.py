from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600

def draw_letter_T(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 40, y)
    glVertex2f(x + 40, y - 10)
    glVertex2f(x, y - 10)
    glVertex2f(x + 15, y)
    glVertex2f(x + 25, y)
    glVertex2f(x + 25, y - 50)
    glVertex2f(x + 15, y - 50)
    glEnd()

def draw_letter_I(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 10, y)
    glVertex2f(x + 10, y - 50)
    glVertex2f(x, y - 50)
    glEnd()

def draw_letter_A(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y - 50)
    glVertex2f(x + 10, y - 50)
    glVertex2f(x + 25, y)
    glVertex2f(x + 15, y)
    glVertex2f(x + 25, y)
    glVertex2f(x + 35, y)
    glVertex2f(x + 50, y - 50)
    glVertex2f(x + 40, y - 50)
    glVertex2f(x + 15, y - 25)
    glVertex2f(x + 35, y - 25)
    glVertex2f(x + 35, y - 30)
    glVertex2f(x + 15, y - 30)
    glEnd()

def draw_letter_N(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 10, y)
    glVertex2f(x + 10, y - 50)
    glVertex2f(x, y - 50)
    glVertex2f(x + 40, y)
    glVertex2f(x + 50, y)
    glVertex2f(x + 50, y - 50)
    glVertex2f(x + 40, y - 50)
    glVertex2f(x + 10, y)
    glVertex2f(x + 20, y)
    glVertex2f(x + 40, y - 50)
    glVertex2f(x + 30, y - 50)
    glEnd()

def draw_name():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.7, 1.0)  # Warna biru terang
    draw_letter_T(-300, 100)
    draw_letter_I(-220, 100)
    draw_letter_T(-180, 100)
    draw_letter_A(-120, 100)
    draw_letter_N(-40, 100)
    glFlush()

def setup():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)

    # Aktifkan antialiasing agar lebih smooth
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

# Main
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL - Nama Panggilan Titan")
setup()
glutDisplayFunc(draw_name)
glutMainLoop()