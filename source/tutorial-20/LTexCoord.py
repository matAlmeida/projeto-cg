from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import *

class LTexCoord (Structure):
	_fields_=[
		('s', GLdouble),
		('t', GLdouble)
	]
	def __init__(self):
		self.s = GLdouble(0.0)
		self.t = GLdouble(0.0)
