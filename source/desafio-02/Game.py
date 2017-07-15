"""

"""

import math as mt
import random as rd
from Pacman import *
from Dot import *

class Game:
    def __init__(self, screenWidth):
        self.__screenWidth = screenWidth

        self.__pacman = Pacman(30)
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
        self.__distancePacToDoc = mt.sqrt(self.__dX**2 + self.__dY**2)

        self.__eatAt = 10

    def __updateDistance(self):
        if(self.__distancePacToDoc < self.__eatAt):
		    self.__updateDotCoord()
        
        return

    def __updateDotCoord(self):
        self.__dotX = rd.randint(50, self.__screenWidth-50)
        self.__dotY = rd.randint(50, self.__screenWidth-50)

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
        self.__distancePacToDoc = mt.sqrt(self.__dX**2 + self.__dY**2)

        return

    def renderDot(self):
        self.__updateDistance()
        self.__dot.render(self.__dotX, self.__dotY)

        return

    def renderPacman(self):
        self.__pacman.render()
        self.__updatePacCoord()
        self.__updateDelta()

        return
