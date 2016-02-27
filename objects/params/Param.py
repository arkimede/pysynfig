import ntpath


class Param:
    def __init__(self):
        self.name = None
        self.value = None
        self.text = None
        self.animated = None
        self.bool = False
	self.node = None

    def setNode(self, node):
	self.node = node

    def getNode(self):
	return self.node

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setValue(self,value):
        self.value = value
	if self.node is not None:
		self.node.set('value', self.value)

    def getValue(self):
        return self.value

    def getText(self):
        return self.text

    def setText(self,text):
        self.text = text

    def setAnimated(self, animated):
       self.animated = animated

    def getAnimated(self):
        return self.animated

    def setBool(self, bool):
        self.bool = bool

    def isBool(self):
        return self.bool

    def pathLeaf(self):
        head, tail = ntpath.split(self.text)
        return tail or ntpath.basename(head)

    def printXML(self):
        if self.getName() is None or self.getValue() is None:
            return ""
        else:
            xml = """\n""" + '<param name=' + self.getName() +'>' + """\n\t""" + '<real value=' + self.getValue() + '/>' + """\n</param>""" + """\n"""
            return xml

