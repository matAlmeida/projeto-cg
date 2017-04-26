from LUntil import *

def main():
	#Initialize FreeGLUT
	glutInit([])

	#Create OpenGL 2.1 context
	glutInitContextVersion( 2, 1 );

	#Create Double Buffered Window
	glutInitDisplayMode(GLUT_DOUBLE)
	glutInitWindowSize(SCREEN_WIDTH,SCREEN_HEIGHT)
	glutCreateWindow("OpenGL")

	#Do post window/context creation initialization
	if(initGL() == False):
		print("Unable to initialize graphics library!\n")
		return 1

	#Set rendering function
	glutDisplayFunc(render)

	#Set main loop
	glutTimerFunc(1000 // SCREEN_FPS, runMainLoop,0)

	#Start GLUT main loop
	glutMainLoop()

	return 0

main()