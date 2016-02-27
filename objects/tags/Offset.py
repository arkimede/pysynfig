from Vector import Vector

class Offset:
    def __init__(self):
        self.animated = None
        self.vector = None

    def getAnimated(self):
        return self.animated

    def setAnimated(self,animated):
        self.animated = animated

    def setVector(self, vector):
        self.vector = vector

    def setVectorX(self,x):
	self.vector.setX(x)

    def setVectorY(self,y):
	self.vector.setY(y)

    def getVector(self):
        return self.vector

    def printXML(self):
        if self.animated is not None:
            xml = """\n""" + "<offset>" + self.animated.printXML() + "</offset>"  + """\n"""
            return xml
        else:
            xml = """\n""" + "<offset>" + self.vector.printXML() + "</offset>" + """\n"""
            return xml
