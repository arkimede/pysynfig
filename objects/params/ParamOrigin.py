from pysynfig.objects.params.Param import Param
from pysynfig.objects.tags.Vector import Vector

class ParamOrigin(Param):

    def __init__(self):
        Param.__init__(self)
        self.vector = None
        self.animated = None

    def setVector(self, x, y, node):
        self.vector = Vector(x,y)
	#workaround to set x and y in vector field node
	self.vector.setNode(node)
	self.setVectorX(x)
	self.setVectorY(y)

    def getVector(self):
        return self.vector

    def setVectorX(self, x):
        self.vector.setX(x)

    def setVectorY(self, y):
        self.vector.setY(y)


    #def setAnimated(self, animated):
    #    self.animated = animated

    #def getAnimated(self):
    #    return self.animated
