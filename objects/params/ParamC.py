__author__ = 'gioacchino'
from ParamChildrenLock import ParamChildrenLock

class ParamC(ParamChildrenLock):

    def __init__(self):
        ParamChildrenLock.__init__(self)