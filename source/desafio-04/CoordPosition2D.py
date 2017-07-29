from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import *

class CoordPosition2D(Structure):
    _fields_=[
        ('x', GLfloat),
        ('y', GLfloat)
    ]
    def __init__(self):
        self.x = GLfloat(0)
        self.y = GLfloat(0)