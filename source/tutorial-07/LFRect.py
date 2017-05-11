from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL.Image import open

class LFRect:
	x = 0
	y = 0
	w = 0
	h = 0

	def getX():
		return self.x
	def getY():
		return self.y
	def getW():
		return self.w
	def getH():
		return self.h