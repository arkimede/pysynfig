__author__ = 'gioacchino'
from Param import Param

class ParamCanvas(Param):

    def __init__(self):
        Param.__init__(self)
        self.layers = []

    def getLayers(self):
        return self.layers

    def setLayers(self, layers):
        self.layers = layers

