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

        self.__player1 = Player("players/boy.png", 50, screenHeight - 51, 8, 0, 30)
        self.__monster = Player("monsters/monster.png", screenWidth, screenHeight - 43, 6, 0, 20)

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

        self.timeMonsters = 0
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
        if(not self.__player1.getStopRender()):
            self.__player1.render()
            if(self.__updateDelta(self.__player1.getCoordX(), self.__player1.getCurrentCoordY(), self.__objX, self.__objY) < 15):
                self.__updateObjCoord()
            return
        else:
            pass

    def renderObjeto(self):
        self.__obj.render(self.__objX, self.__objY)

        return

    def renderMonster(self):
        if(not self.__monster.getStopRender()):
            self.__monster.render()
            self.monstroAnda()
            return
        else:
            self.updateTimeMonsters()

    def monstroAnda(self):
        if(not self.__monster.getDead() and not self.__player1.getDead()):
            if(self.__player1.getCoordX() > self.__monster.getCoordX() - 20 and self.__player1.getCoordX() < self.__monster.getCoordX() + 20):
                if(self.__player1.getCurrentCoordY() < self.__monster.getCurrentCoordY()-30):
                    self.__player1.setCurrentCoordY(self.__monster.getCurrentCoordY()-30)
                    self.__monster.changeCharacter("monsters/deadMonster.png", 4, self.__monster.getCoordX(), self.__screenHeight - 38, 20)
                    self.__monster.setDead(True)
                else:
                    self.__player1.changeCharacter("players/blood.png", 6, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
                    self.__player1.setDead(True)
            
            
            self.__monster.setCoordX(self.__monster.getCoordX() - 1)

    def renderSuperficie(self, x, y):
        self.__superficie.render(x, y)

        return

    def __updateObjCoord(self):
        self.__objX = rd.randint(50, self.__screenWidth - 50)
        self.__objY = rd.randint(self.__player1.getPuloMax(), self.__player1.getCoordY())

        return

    def updateTimeMonsters(self):
            self.timeMonsters += 1
            if(self.timeMonsters > 150):
                self.timeMonsters = 0
                self.__monster.changeCharacter("monsters/monster.png", 6, self.__screenWidth, self.__screenHeight - 43, 20)
                self.__monster.setDead(False)
                self.__monster.setStopRender(False)

    def callHandleKeys(self, key):
        velocidade = 6
        key = ord(key)

        #PLAYER 1
        if(not self.__player1.getDead()):
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

            #se o usuario pressiona 1
            elif(key == 49):
                self.__player1.changeCharacter("players/boy.png", 8, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
            elif(key == 50):
                self.__player1.changeCharacter("players/girl.png", 6, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
            elif(key == 51):
                self.__player1.changeCharacter("players/mario.png", 7, self.__player1.getCoordX(), self.__screenHeight - 51, 25)
            elif(key == 116): #T
                self.__player1.changeCharacter("players/transparent.png", 7, self.__player1.getCoordX(), self.__screenHeight - 57,  35)