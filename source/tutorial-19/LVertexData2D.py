from LVertexPos2D import *
from LTexCoord import *

class LVertexData2D(Structure):
	_fields_=[
		('position', LVertexPos2D),
		('texCoord', LTexCoord)
	]
	def __init__(self):
		self.position = LVertexPos2D()
		self.texCoord = LTexCoord()
