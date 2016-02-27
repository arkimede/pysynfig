class Keyframe:
    def __init__(self):
        self.time = None
        self.active = None

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def setActive(self, active):
       self.active = active

    def getActive(self):
       return self.active

