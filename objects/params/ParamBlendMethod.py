from Param import Param

class ParamBlendMethod(Param):

    def __init__(self):
        Param.__init__(self)
        self.static = None


    def setStatic(self, static):
        self.static = static
	if self.node is not None:
		self.node.set('static', self.static)

    def getStatic(self):
        return self.static
