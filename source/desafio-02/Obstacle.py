from Pacman import *

class Obstacle:
	def __init__(self, objType = GL_QUADS, size = 10, color = [0,0,0], position = [0,0]):
		"""
        Construct a new 'Obstacle' object.

        :param objType: The type of rendering object
        :param size: The size of obstacle
        :param color: A vector with RGB values. [0:255, 0:255, 0:255]
        :param position: The position of obstacle in the screen
        """
		self.__type = objType
		self.__size = size
		self.__color = color
		self.__position = position

	def render(self):
		#Defining the start position
		glTranslatef(self.__position[0],self.__position[1],0)

		#Setting the obstacle's color
		glColor3f(self.__color[0], self.__color[1], self.__color[2])
		
		#Render the object type choosed
		glBegin(self.__type)
		glVertex2f(0,0)
		glVertex2f(self.__size,0)
		glVertex2f(self.__size,self.__size)
		glVertex2f(0,self.__size)
		glEnd();