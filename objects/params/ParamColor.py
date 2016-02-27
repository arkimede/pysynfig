from pysynfig.objects.params import Param
from pysynfig.objects.tags import Color

class ParamColor(Param):

    def __init__(self):
        Param.__init__(self)
        self.color = None

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def printXML(self):
        if self.color is None:
            return ""
        else:
            xml = """\n""" + "<param name=" + self.getName() + ">\n" + self.color.printXML() + "</param>\n"
            return xml
