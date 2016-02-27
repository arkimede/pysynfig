from Waypoint import Waypoint

class Animated:

    def __init__(self):
        self.type = None
        self.waypointList = []

    def setType(self, type):
        self.type = type
    
    def getType(self):
        return self.type

    def getWaypoint(self):
        return self.waypointList

    def addWaypoint(self, waypoint):
        self.waypointList.append(waypoint)

    def printXML(self):
        xml = """\n""" + "<animated type=" + self.type + ">"
        for tmpWay in self.waypointList:
            xml = xml + tmpWay.printXML()
        return xml
