from CoordPosition2D import *

class Sprite(Structure):
    _fields_=[
        ('coord', CoordPosition2D*4)
    ]
    def __init__(self):
        self.coord = (CoordPosition2D*4)()