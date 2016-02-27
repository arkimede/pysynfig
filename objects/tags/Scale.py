class Scale:
    def __init__(self):
        self.animated = None
        self.vector = None
    
    def setVector(self, vector):
        self.vector = vector

    def getVector(self):
        return self.vector

    def setAnimated(self, animated):
        self.animated = animated

    def getAnimated(self):
        return self.animated

    def setVectorX(self,x):
	self.vector.setX(x)

    def setVectorY(self,y):
	self.vector.setY(y)

    def printXML(self):
        if self.animated is not None:
            xml = """\n""" + "<scale>" + self.animated.printXML() + "</scale>\n" 
            return xml
        else:
            xml = """\n""" + "<scale>" + self.vector.printXML() + "</scale>" + """\n"""
            return xml
