import pygame
import pygame.locals
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
import OpenGL.GLUT.freeglut

def initGL():
	#Initialize Projection Matrix
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
    
	#Initialize Modelview Matrix
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
	#Initialize clear color
	glClearColor(0,0,0,1)
	
	#Check for error
	erro = glGetError()
	if(erro != GL_NO_ERROR):
		print("Error initializing OpenGL! %s\n", gluErrorString(erro))
		return False
	return True

def update():
	return 0

def render():
	#Clear color buffer
	glCLear(GL_COLOR_BUFFER_BIT)

	#Render quad
	glBegin(GL_QUADS)
	glVertex2f(-0.5,-0.5)
	glVertex2f(0.5,-0.5)    	
	glVertex2f(0.5,0.5)
	glVertex2f(-0.5,0.5)
	glEnd()

	#Update screen
	glutSwapBuffers()

def runMainLoop(val):
	#Frame logic
	update()
	render()

	#Run frame one more time
	glutTimerFunc(1000 / SCREEN_FPS, runMainLoop, val)