class Angle:
    def __init__(self):
        self.value = None
        self.animated = None
    	self.node = None

    def setNode(self, node):
	self.node = node

    def getNode(self):
	return self.node

    def setValue(self, value):
        self.value = value
	if self.node is not None:
		self.node.set('value', value)

    def getValue(self):
        return self.value

    def setAnimated(self, animated):
        self.animated = animated

    def getAnimated(self):
        return self.animated

    def printXML(self):
        if self.animated is not None:
            xml = """\n""" + "<angle>" + self.animated.printXML() + "</angle>\n"
            #return xml
        elif self.value is not None:
            xml = """\n""" + """<angle>\n\t<angle value=""" + self.value +"/>\n" + """</angle>\n"""
        return xml
