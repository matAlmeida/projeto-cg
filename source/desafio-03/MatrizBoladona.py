from OpenGL.GL import *

class MatrizBoladona(object):

    def __enter__(self):
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glLoadIdentity()

        #Salvando matriz padrão
        glPushMatrix()

    def __exit__(self, x, y, z):
        glBindTexture(GL_TEXTURE_2D,0)