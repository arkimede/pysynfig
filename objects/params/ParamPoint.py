from pysynfig.objects.params.Param import Param
from pysynfig.objects.tags.Point import Point

class ParamPoint(Param):

    def __init__(self):
        Param.__init__(self)
        self.point = None

    def getPoint(self):
        return self.point

    def setPoint(self, point):
        self.point = point

    def printXML(self):
        if self.point is None:
            return ""
        else:
            xml = """\n""" + "<param name=" + self.getName() + ">\n" + self.point.printXML() + "</param>\n"
            return xml
