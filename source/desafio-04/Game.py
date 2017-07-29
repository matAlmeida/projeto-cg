"""

"""

import math as mt
import random as rd
from Pacman import *
from Dot import *
from Objeto import *
from Superficie import *

class Game:
    def __init__(self, screenWidth,screenHeight):
        self.__screenWidth = screenWidth
        self.__screenHeight = screenHeight

        self.__dot = Dot(50, screenHeight - 55, 1, 30)

        self.__obj = Objeto("aboboratemp.png")
        self.__objX = 0
        self.__objY = 0
        self.__updateObjCoord()

        self.__superficie = Superficie("fundo.jpg")
        self.__superficieX = 0
        self.__superficieY = 0
        
        self.__pacman = Pacman(30,4)
        self.__pacX = 0
        self.__pacY = 0
        self.__pacmanDirection = 0

        self.__eatAt = 1

    def __updateDistance(self):
        if(self.__distanceObjToDot < self.__eatAt):
        	self.__updateDotCoord()
        
        return

    def __updateDelta(self, x1, y1, x2, y2):
        dX = x1 - x2
        dY = y1 - y2
        distanceObjToDot = mt.sqrt(dX**2 + dY**2)
        return distanceObjToDot

    def renderDot(self):
        self.__dot.render()
        if(self.__updateDelta(self.__dot.getCoordX(), self.__dot.getCoordY(), self.__objX, self.__objY) < 15):
            self.__updateObjCoord()
        return

    def renderObjeto(self):
        self.__obj.render(self.__objX, self.__objY)

        return

    def renderSuperficie(self, x, y):
        self.__superficie.render(x, y)

        return

    def __updateObjCoord(self):
        self.__objX = rd.randint(50, self.__screenWidth - 50)
        self.__objY = rd.randint(self.__dot.getPuloMax(), self.__dot.getCoordY())

        return

    def callHandleKeys(self, key):
        self.__dot.handlekeys(key)