import math as mt
import random as rd
from Pacman import *
from Player import *
from Objeto import *
from Superficie import *

class Game:
    def __init__(self, screenWidth,screenHeight):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.init()
        pygame.mixer.init()
        music = pygame.mixer.music.load(b'musics/jogo.wav')
        pygame.mixer.music.play(-1)
        self.shotEffect = pygame.mixer.Sound(b'musics/shot.wav')
        self.jumpEffect = pygame.mixer.Sound(b'musics/jump.wav')
        self.deadMonsterEffect = pygame.mixer.Sound(b'musics/deadMonster.wav')
        self.deadPlayerEffect = pygame.mixer.Sound(b'musics/deadPlayer.wav')
        self.getItemEffect = pygame.mixer.Sound(b'musics/coin.wav')

        self.__screenWidth = screenWidth
        self.__screenHeight = screenHeight

        self.__player1 = Player("players/boy.png", 50, screenHeight - 51, 8, 0, 30)

        self.monsterType = 1
        self.__monster = Player("monsters/monster.png", screenWidth, screenHeight - 43, 6, 0, 20)
        self.__monster.setVelocity(1)

        self.__objX = rd.randint(50, self.__screenWidth - 50)
        self.__objY = rd.randint(self.__player1.getPuloMax(), self.__player1.getCoordY())
        self.__updateObjType()
        self.__obj = Objeto(self.objType, self.__objX, self.__objY)

        self.__shot = Objeto(0, self.__player1.getCoordX() + 10, self.__player1.getCurrentCoordY())

        self.__superficie = Superficie("fundo.jpg")
        self.__superficieX = 0
        self.__superficieY = 0
        
        self.__pacman = Pacman(30,4)
        self.__pacX = 0
        self.__pacY = 0
        self.__pacmanDirection = 0

        self.timeMonsters = 0
        self.__eatAt = 1

        self.theEnd = False

    def __updateDistance(self):
        if(self.__distanceObjToDot < self.__eatAt):
            self.__updateDotCoord()
        
        return

    def __updateObjType(self):
        self.objType = rd.randint(1,5)

    def __updateDelta(self, x1, y1, x2, y2):
        dX = x1 - x2
        dY = y1 - y2
        distanceObjToDot = mt.sqrt(dX**2 + dY**2)
        return distanceObjToDot

    def renderPlayer1(self):
        if(not self.__player1.getStopRender()):
            self.__player1.render()
            if(self.__updateDelta(self.__player1.getCoordX(), self.__player1.getCurrentCoordY(), self.__objX, self.__objY) < 15):
                self.getItemEffect.play(0)
                self.__updateObjCoord()
            return
        else:
            pass

    def renderObjeto(self):
        self.__obj.render()

        return

    def renderShot(self):
        if(not self.__shot.getStopRender()):
            self.__shot.render()
            if(self.__updateDelta(self.__shot.getCoordX(), self.__shot.getCoordY(), self.__monster.getCoordX(), self.__monster.getCoordY()) < 20):
                self.chooseMonster(self.monsterType, True)
                self.__monster.setDead(True)
                self.__shot.setStopRender(True)
                self.deadMonsterEffect.play(0)
            self.moveShot()
            return
        else:
            pass

    def moveShot(self):
        if(self.__shot.getRotacionar()):
            self.__shot.setCoordX(self.__shot.getCoordX() - 5)
        else:
            self.__shot.setCoordX(self.__shot.getCoordX() + 5)

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
                    if(not self.__monster.getImage() == "monsters/boo.png"):
                        self.__player1.setCurrentCoordY(self.__monster.getCurrentCoordY()-30)
                        self.chooseMonster(self.monsterType, True)
                        self.__monster.setDead(True)
                        self.deadMonsterEffect.play(0)
                else:
                    self.__player1.changeChapter("players/blood.png", 6, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
                    self.__player1.setDead(True)
                    self.deadPlayerEffect.play(0)
            
            
            self.__monster.setCoordX(self.__monster.getCoordX() - self.__monster.getVelocity())

    def renderSuperficie(self, x, y):
        self.__superficie.render(x, y)

        return

    def __updateObjCoord(self):
        self.__objX = rd.randint(50, self.__screenWidth - 50)
        self.__objY = rd.randint(self.__player1.getPuloMax(), self.__player1.getCoordY())
        self.__updateObjType()
        self.__obj.changeObj(self.objType, self.__objX, self.__objY)

        return

    def updateTimeMonsters(self):
            self.timeMonsters += 1
            if(self.timeMonsters > 150):
                self.timeMonsters = 0
                self.monsterType = rd.randint(1,8)
                self.chooseMonster(self.monsterType, False)
                self.__monster.setDead(False)
                self.__monster.setStopRender(False)

    def callHandleKeys(self, key):
        key = ord(key)

        #PLAYER 1
        if(not self.__player1.getDead()):
            #se o usuario pressiona a
            if(key == 97):
                self.__player1.setAndando(True)
                if(self.__player1.getDireita()):
                    self.__player1.setRotacionar(True)
                self.__player1.setDireita(False)
                self.__player1.setCoordX(self.__player1.getCoordX() - self.__player1.getVelocity())
            #se o usuario pressiona d
            elif(key == 100):
                self.__player1.setAndando(True)
                if(not self.__player1.getDireita()):
                    self.__player1.setRotacionar(False)
                self.__player1.setDireita(True)
                self.__player1.setCoordX(self.__player1.getCoordX() + self.__player1.getVelocity())
            #se o usuario pressiona w
            elif(key == 119):
                self.__player1.setPular(True)
                self.jumpEffect.play(0)
            #se o usuario pressiona e
            elif(key == 101):
                if(self.__player1.getImage() == "players/droid.png"):
                    self.shotEffect.play(0)
                    self.__shot.setRotacionar(self.__player1.getRotacionar())
                    self.__shot.setStopRender(False)
                    if(self.__shot.getRotacionar()):
                        self.__shot.setCoordX(self.__player1.getCoordX() - 50)
                    else:
                        self.__shot.setCoordX(self.__player1.getCoordX() + 50)
                    self.__shot.setCoordY(self.__player1.getCurrentCoordY())

            #se o usuario pressiona 1
            elif(key == 49):
                self.__player1.changeChapter("players/boy.png", 8, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
            elif(key == 50):
                self.__player1.changeChapter("players/girl.png", 6, self.__player1.getCoordX(), self.__screenHeight - 51, 30)
            elif(key == 51):
                self.__player1.changeChapter("players/mario.png", 7, self.__player1.getCoordX(), self.__screenHeight - 51, 25)
            elif(key == 52):
                self.__player1.changeChapter("players/droid.png", 10, self.__player1.getCoordX(), self.__screenHeight - 60, 35)
            elif(key == 116): #T
                self.__player1.changeChapter("players/transparent.png", 7, self.__player1.getCoordX(), self.__screenHeight - 57, 35)
        #FIM DE JOGO - Tecla Enter
        elif(key == 13):
            self.theEnd = True

    def chooseMonster(self, op, dead):
        if(op == 1):
            if(dead):
                self.__monster.changeChapter("monsters/deadMonster.png", 4, self.__monster.getCoordX(), self.__screenHeight - 38, 20)
            else:
                self.__monster.changeChapter("monsters/monster.png", 6, self.__screenWidth, self.__screenHeight - 43, 20)
                self.__monster.setVelocity(1)
        elif(op == 2):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 50, 50)
            else:
                self.__monster.changeChapter("monsters/zombie.png", 3, self.__screenWidth, self.__screenHeight - 75, 50)
                self.__monster.setVelocity(1)
        elif(op == 3):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 50, 50)
            else:
                self.__monster.changeChapter("monsters/zombie2.png", 3, self.__screenWidth, self.__screenHeight - 75, 50)
                self.__monster.setVelocity(1)
        elif(op == 4):
            if(dead):
                self.__monster.changeChapter("monsters/deadBoo.png", 10, self.__monster.getCoordX(), self.__screenHeight - 54, 30)
            else:
                self.__monster.changeChapter("monsters/boo.png", 8, self.__screenWidth, self.__screenHeight - 54, 30)
                self.__monster.setVelocity(2)
        elif(op == 5):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 65, 30)
            else:
                self.__monster.changeChapter("monsters/bat.png", 2, self.__screenWidth, self.__screenHeight - 60, 30)
                self.__monster.setVelocity(3)
        elif(op == 6):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 70, 40)
            else:
                self.__monster.changeChapter("monsters/dragon.png", 3, self.__screenWidth, self.__screenHeight - 65, 40)
                self.__monster.setVelocity(1)
        elif(op == 7):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 70, 40)
            else:
                self.__monster.changeChapter("monsters/dragon2.png", 3, self.__screenWidth, self.__screenHeight - 65, 40)
                self.__monster.setVelocity(1)
        elif(op == 8):
            if(dead):
                self.__monster.changeChapter("monsters/blood.png", 4, self.__monster.getCoordX(), self.__screenHeight - 65, 20)
            else:
                self.__monster.changeChapter("monsters/eye.png", 3, self.__screenWidth, self.__screenHeight - 70, 20)
                self.__monster.setVelocity(3)

    def getTheEnd(self):
        return self.theEnd
