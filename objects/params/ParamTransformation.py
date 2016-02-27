from Param import Param

class ParamTransformation(Param):

    def __init__(self):
        Param.__init__(self)
        self.composite = None

    def setComposite(self, composite):
        self.composite = composite

    def getComposite(self):
        return self.composite

    def printXML(self):
        if self.composite is None:
            return ""
        else:
            xml = """\n""" + "<param name=" + self.getName() + ">\n" + self.composite.printXML() + "</param>\n"
            return xml
