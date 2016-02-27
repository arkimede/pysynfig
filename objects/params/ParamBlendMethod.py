from Param import Param

class ParamBlendMethod(Param):

    def __init__(self):
        Param.__init__(self)
        self.static = None


    def setStatic(self, static):
        self.static = static

    def getStatic(self):
        return self.static
