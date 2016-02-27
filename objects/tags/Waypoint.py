from Vector import Vector

class Waypoint:

    def __init__(self):
        self.time = None
        self.before = None
        self.after = None
        self.vector = None
        self.value = None
        self.parentType = None

    def setVector(self, vector):
        self.vector = vector

    def getVector(self):
        return self.vector

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def setBefore(self, before):
        self.before = before

    def getBefore(self):
        return self.before
    
    def setAfter(self, after):
        self.after = after

    def getAfter(self):
        return self.after

    def setParentType(self, parentType):
        self.parentType = parentType

    def getParentType(self):
        return self.parentType

    def printXML(self):
        xml = """\n""" + "<waypoint time=" + self.time + " before=" + self.before + " after=" + self.after + ">"
        if self.vector is not None:
            xml += self.vector.printXML()
        else:
            xml += """\n\t""" + "<" + self.parentType + " value=" + self.value + ">\n"
        xml += "</waypoint>\n"
        return xml
