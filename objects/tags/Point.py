from Vector import Vector

class Point:
    def __init__(self, vector):
        self.vector = vector

    def setVector(self, vector):
        self.vector = vector

    def getVector(self):
        return self.vector

    def printXML(self):
        return self.vector.printXML()
