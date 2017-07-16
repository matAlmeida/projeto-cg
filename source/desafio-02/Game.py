"""

"""

import random as rd
from Pacman import *
from Dot import *
from Obstacle import *

class Game:
    def __init__(self, screenWidth,screenHeight):
        """
        Game render a "Pacman Game" in the screen and automates the Pacman's movements toward dots

        :param screenWidth: The Width of the window where the game will be rendered
        :param screenHeight: The Height of the window where the game will be rendered
        """
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

    def __updateDotCoord(self):
        """
        Sets the new Dot's coordinates before re-render.
        """
        if(self.__distancePacToDot < self.__eatAt):
            self.__dotX = rd.randint(50, self.__screenWidth-50)
            self.__dotY = rd.randint(50, self.__screenHeight-50)

        return

    def __updatePacCoord(self):
        """
        Updates the Pacman's coordinates to re-render after move.
        """
        pos = self.__pacman.getPos()
        self.__pacX = pos[0]
        self.__pacY = pos[1]

        return

    def __movePacman(self):
        """
        Change the Pacman's direction using the Dot's position.
        """
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
        """
        Updates the distances between the Pacman and the Dot.
        """
        self.__dX = self.__dotX - self.__pacX
        self.__dY = self.__dotY - self.__pacY
        self.__distancePacToDot = mt.sqrt(self.__dX**2 + self.__dY**2)

        return

    def __velocityControl(self):
        """
        ?
        """
    	if(self.__dX < self.__pacman.getCurrentMovSpeed() and self.__dX > 0):
    		self.__pacman.setCurrentMovSpeed(self.__dX)
    	elif(self.__dY < self.__pacman.getCurrentMovSpeed() and self.__dY > 0):
    		self.__pacman.setCurrentMovSpeed(self.__dY)
    	else:
    		self.__pacman.initCurrentMovSpeed()

        return
    
    def getDistance(self):
        """
        Returns the current distance between the Pacman and the Dot.

        :return: Current distance between the Pacman and the Dot
        """

        return self.__distancePacToDot

    def renderObstacles(self):
        """
        Render Obstacles in the screen.
        """
    	self.__obstacle.render()

        return

    def renderDot(self):
        """
        Render the Dot in the screen.
        """
        self.__updateDotCoord()
        self.__dot.render(self.__dotX, self.__dotY)

        return

    def renderPacman(self):
        """
        Render the Pacman in the screen.
        """
    	self.__velocityControl()
    	self.__pacman.render()
    	self.__updatePacCoord()
    	self.__movePacman()
    	self.__updateDelta()
    	self.__pacman.initCurrentMovSpeed()

    	return