class MainCanvas:

    def __init__(self):
        self.id = None
        self.guid = None
        self.version = None
        self.width = None
        self.height = None
        self.xres = None
        self.yres = None
        self.fps = None
        self.start_time = None
        self.begin_time = None
        self.end_time = None
        self.antialias = None
        self.view_bow = None
        self.bg_color = None
        self.focus = None
        
        self.name = None
        self.meta = []
        self.keyframe = None

    def setMeta(self, metaList):
        self.meta = metaList

    def getMeta(self):
        return meta

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setKeyframe(self, keyframe):
        self.keyframe = keyframe
    
    def getKeyframe(self):
        return self.keyframe

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getGuid(self):
        return self.guid

    def setGuid(self, guid):
        return self.guid

    def setVersion(self, version):
        self.version = version

    def getVersion(self):
        return self.version

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setXres(self, xres):
        self.xres = xres

    def getXres(self):
        return self.xres

    def setYres(self, yres):
        self.yres = yres

    def getYres(self):
        return self.yres

    def setFps(self, fps):
        self.fps = fps

    def getFps(self):
        return self.fps

    def getStartTime(self):
        return self.start_time

    def setStartTime(self, start_time):
        return self.start_time

    def setBeginTime(self, begin_time):
        self.begin_time = begin_time

    def getBeginTime(self):
        return self.begin_time

    def setAntialias(self, antialias):
        self.antialias = antialias

    def getAntialias(self):
        return self.antialias

    def getViewBox(self):
        return self.view_bow

    def setViewBox(self, view_box):
        self.view_bow = view_bow

    def getBgColor(self):
        return self.bg_color

    def setBgColor(self, bg_color):
        self.bg_color = bg_color

    def setFocus(self, focus):
        self.focus = focus

    def getFocus(self):
        return self.focus

        
