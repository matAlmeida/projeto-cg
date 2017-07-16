"""

"""

import random as rd
from Pacman import *
from Dot import *
from Obstacle import *

class Game:
    def __init__(self, screenWidth,screenHeight):
        self.__screenWidth = screenWidth
        self.__screenHeight = screenHeight

        self.__obstacle = Obstacle(GL_LINE_LOOP, 100, [1,1,1], [screenWidth//2-50, screenHeight//2-50])

        self.__pacman = Pacman(30,4)
        self.__pacX = 0
        self.__pacY = 0
        self.__updatePacCoord()
        self.__pacmanDirection = 0

        self.__dot = Dot()
        self.__dotX = 0
        self.__dotY = 0
        self.__updateDotCoord()

        self.__dX = self.__dotX - self.__pacX
        self.__dY = self.__dotY - self.__pacY
        self.__distancePacToDot = mt.sqrt(self.__dX**2 + self.__dY**2)

        self.__eatAt = 1

    def __updateDistance(self):
        if(self.__distancePacToDot < self.__eatAt):
        	self.__updateDotCoord()
        
        return

    def getDistance():
    	return self.__distancePacToDot

    def __updateDotCoord(self):
        self.__dotX = rd.randint(50, self.__screenWidth-50)
        self.__dotY = rd.randint(50, self.__screenHeight-50)

        return

    def __updatePacCoord(self):
        pos = self.__pacman.getPos()
        self.__pacX = pos[0]
        self.__pacY = pos[1]

        return

    def __movePacman(self):
        self.__updateDelta()

        if(self.__dX > 0):
            self.__pacmanDirection = 0
        elif(self.__dX < 0):
            self.__pacmanDirection = 180
        elif(self.__dY < 0):
            self.__pacmanDirection = 270
        elif(self.__dY > 0):
            self.__pacmanDirection = 90

        self.__pacman.changeDirection(self.__pacmanDirection)

        return

    def __updateDelta(self):
        self.__dX = self.__dotX - self.__pacX
        self.__dY = self.__dotY - self.__pacY
        self.__distancePacToDot = mt.sqrt(self.__dX**2 + self.__dY**2)

        return

    def renderObstacles(self):
    	self.__obstacle.render()

    def renderDot(self):
        self.__updateDistance()
        self.__dot.render(self.__dotX, self.__dotY)

        return

    def renderPacman(self):
    	self.__velocityControl()
    	self.__pacman.render()
    	self.__updatePacCoord()
    	self.__movePacman()
    	self.__updateDelta()
    	self.__pacman.initCurrentMovSpeed()

    	return

    def __velocityControl(self):
    	diferenca = []
    	diferenca.append(self.__dX)
    	diferenca.append(self.__dY)
    	if(diferenca[0] < self.__pacman.getcurrentMovSpeed() and diferenca[0] > 0):
    		self.__pacman.setcurrentMovSpeed(diferenca[0])
    	elif(diferenca[1] < self.__pacman.getcurrentMovSpeed() and diferenca[1] > 0):
    		self.__pacman.setcurrentMovSpeed(diferenca[1])
    	else:
    		self.__pacman.initCurrentMovSpeed()