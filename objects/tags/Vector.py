class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y


    def getX(self):
        return self.x


    def getY(self):
        return self.y


    def setX(self,x):
        self.x = x


    def setY(self,y):
        self.y = y

    def printXML(self):
        xml = """\n""" + "<vector>" + """\n\t""" + "<x>" + self.x + "</x>" +  """\n\t""" + "<y>" + self.y + "</y>\n" + "</vector>" + """\n"""
        return xml

