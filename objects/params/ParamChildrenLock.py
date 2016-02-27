__author__ = 'gioacchino'
from Param import Param

class ParamChildrenLock(Param):

    def __init__(self):
        Param.__init__(self)
        self.static = None

    def getStatic(self):
        return self.static

    def setStatic(self,static):
        self.static = static
