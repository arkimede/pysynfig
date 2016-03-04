from pysynfig.reader import XmlParser

class Interface:
	def __init__(self, filename):
		self.filename = filename
		self.list = None
		self.mainCanvas = None
		self.parser = None

	def write(self):
		self.parser.tree.write(self.filename)

	def read(self):
		self.parser = XmlParser(self.filename)
		self.parser.parse()

		#self.mainCanvas = parser.getMainCanvas()

		self.parser.getLayers(self.parser.tree, self.parser.listLayer)
		self.list = self.parser.getListLayers()
		
	def layer(self,selector):
		if type(selector) is str:
			#in this case selector is the name of the layer
			#not implemented
			pass
		elif type(selector) is int:
			#in this case selector is the index in the list
			return self.list[selector]

	def main_canvas(self):
		return self.mainCanvas



