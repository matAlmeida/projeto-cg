"""

"""

import math as mt
import random as rd
from Pacman import *
from Player import *
from Objeto import *
from Superficie import *

class Game:
    def __init__(self, screenWidth,screenHeight):
        self.__screenWidth = screenWidth
        self.__screenHeight = screenHeight

        self.__player1 = Player("boy.png", 50, screenHeight - 51, 8, 0, 30)
        self.__player2 = Player("walk.png", 50, screenHeight - 55, 6, 1, 30)

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

    def renderPlayer1(self):
        self.__player1.render()
        if(self.__updateDelta(self.__player1.getCoordX(), self.__player1.getCurrentCoordY(), self.__objX, self.__objY) < 15):
            self.__updateObjCoord()
        return

    def renderPlayer2(self):
        self.__player2.render()
        if(self.__updateDelta(self.__player2.getCoordX(), self.__player2.getCurrentCoordY(), self.__objX, self.__objY) < 15):
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
        self.__objY = rd.randint(self.__player1.getPuloMax(), self.__player1.getCoordY())

        return

    def callHandleKeys(self, key):
        velocidade = 6
        key = ord(key)

        #PLAYER 1
        #se o usuario pressiona a
        if(key == 97):
            self.__player1.setAndando(True)
            if(self.__player1.getDireita()):
                self.__player1.setRotacionar(True)
            self.__player1.setDireita(False)
            self.__player1.setCoordX(self.__player1.getCoordX() - velocidade)
        #se o usuario pressiona d
        elif(key == 100):
            self.__player1.setAndando(True)
            if(not self.__player1.getDireita()):
                self.__player1.setRotacionar(False)
            self.__player1.setDireita(True)
            self.__player1.setCoordX(self.__player1.getCoordX() + velocidade)
        #se o usuario pressiona w
        elif(key == 119):
            self.__player1.setPular(True)

        #se o usuario pressiona s
        #elif(key == 115):
            #self.__dot.setCoordY(self.__dot.getCoordY + 16)