from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class PonteiroVertex():
	def __init__(self, hms):
		self.hms = hms

	def render(self):
		glBegin(GL_LINES)
		glColor3f(1,0,0)
		glVertex2f(50,100)
		glColor3f(1,0,0)
		glVertex2f(150,200)
		glEnd()