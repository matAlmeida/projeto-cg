from Pacman import *

class Obstacle:
	def __init__(self, objType = GL_QUADS, size = 10, color = [0,0,0], position = [0,0]):
		self.__type = objType
		self.__size = size
		self.__color = color
		self.__position = position

	def render(self):
		#Definindo inicio da renderização
		glTranslatef(self.__position[0],self.__position[1],0)

		#Definindo a cor do objeto
		glColor3f(self.__color[0], self.__color[1], self.__color[2])
		
		#Renderizando de acordo com o tipo escolhido
		glBegin(self.__type)
		glVertex2f(0,0)
		glVertex2f(self.__size,0)
		glVertex2f(self.__size,self.__size)
		glVertex2f(0,self.__size)
		glEnd();