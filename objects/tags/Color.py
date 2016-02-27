class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def setRed(self, red):
        self.red = red

    def getRed(self):
        return self.red

    def setGreen(self, green):
        self.green = green

    def getGreen(self):
        return self.green

    def setBlue(self, blue):
        self.blue = blue

    def getBlue(self):
        return self.blue

    def setAlpha(self, alpha):
        self.alpha = alpha

    def getAlpha(self):
        return self.alpha

    def setVector(self, vector):
        self.vector = vector

    def getVector(self):
        return self.vector

    def printXML(self):
        xml = """\n""" + "<color>\n\t<r>" + self.red + "</r>\n\t<g>" + self.green + "</g>\n\t<b>" + self.blue + "</b>\n\t<a>" + self.alpha + "</a>\n</color>" + """\n"""
        return xml
