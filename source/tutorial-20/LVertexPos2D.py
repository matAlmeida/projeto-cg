from OpenGL.GL import *
from ctypes import *

class LVertexPos2D(Structure):
	_fields_ = [
		('x', GLdouble),
		('y', GLdouble)
	]
	def __init__(self):
		self.x = GLdouble(0.0)
		self.y = GLdouble(0.0)

