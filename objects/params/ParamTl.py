__author__ = 'gioacchino'
from Param import Param

class ParamTl(Param):

    def __init__(self):
        Param.__init__(self)
        self.vector = None

    def getVector(self):
        return self.vector

    def setVector(self, vector):
        self.vector = vector

    def setVectorX(self,x):
	if self.vector is not None:
		self.vector.setX(x)

    def setVectorY(self,y):
	if self.vector is not None:
        	self.vector.setY(y)
