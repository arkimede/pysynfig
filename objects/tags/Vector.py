class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
	self.node = None

    def __init__(self,x,y,node=None):
	self.x = x
	self.y = y
	self.node = node

    def setNode(self, node):
	self.node = node

    def getNode(self):
	return self.node

    def getX(self):
        return self.x


    def getY(self):
        return self.y


    def setX(self,x):
        self.x = x
	if self.node is not None:
		self.node.find('x').text = self.x


    def setY(self,y):
        self.y = y
        if self.node is not None:
		self.node.find('y').text = self.y


    def printXML(self):
        xml = """\n""" + "<vector>" + """\n\t""" + "<x>" + self.x + "</x>" +  """\n\t""" + "<y>" + self.y + "</y>\n" + "</vector>" + """\n"""
        return xml

