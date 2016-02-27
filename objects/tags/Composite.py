import pdb
class Composite:

   def __init__(self):
        self.offset = None
        self.angle = None
        self.skew_angle = None
        self.scale = None
        self.type = None
    
   def setType(self,type):
        self.type = type

   def getType(self):
        return self.type

   def setOffset(self, offset):
        self.offset = offset

   def getOffset(self):
       return self.offset

   def getAngle(self):
       return self.angle

   def setAngle(self, angle):
       self.angle = angle

   def setSkewAngle(self, skew_angle):
       self.skew_angle = skew_angle

   def getSkewAngle(self):
       return self.skew_angle

   def setScale(self, scale):
       self.scale = scale

   def getScale(self):
       return self.scale

   def printXML(self):
       xml = """\n""" + "<composite type=" + self.type + ">" + self.offset.printXML() + self.angle.printXML() + self.skew_angle.printXML() + self.scale.printXML() + "</composite>" + """\n"""
       return xml
