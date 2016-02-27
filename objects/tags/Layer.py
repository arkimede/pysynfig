from treedict import TreeDict

class Layer:
    
    def __init__(self):
        self.type = None
        self.active = None
        self.exclude_from_rendering = None
        self.version = None
        self.desc = None
        self.HashParam = {} #hash di tutti i param del layer
        self.treeObj = TreeDict()
        self.zMax = None
        self.filenameParamImportLayer = None

    def setZmax(self,zMax):
        self.zMax = zMax

    def getZmax(self):
        return self.zMax

    def setType(self,type):
        self.type = type

    def getType(self):
        return self.type

    def setActive(self,active):
        self.active = active
    
    def getActive(self):
        return self.active

    def setExcludeFromRendering(self,efr):
        self.exclude_from_rendering = efr

    def getExcludeFromRendering(self):
        return self.exclude_from_rendering

    def setVersion(self, version):
        self.version = version

    def getVersion(self):
        return self.version

    def setDesc(self, desc):
        self.desc = desc

    def getDesc(self):
        return self.desc

    def getHashParam(self):
        return self.HashParam

    def addParam(self,param):
        self.HashParam[param.name] = param

    def getParam(self,paramName):
        return self.HashParam[paramName]

    def getFilenameParamImportLayer(self):
        return self.filenameParamImportLayer

    def setFilenameParamImportLayer(self, filenameParamImportLayer):
        self.filenameParamImportLayer = filenameParamImportLayer

    def getParamFilename(self):
        tmpFilename = self.HashParam.get('filename')
        if tmpFilename is not None:
            return tmpFilename
        else:
            return self.filenameParamImportLayer

    def get(self, name):
        if name == "offset":
            transformation = self.getParam("transformation")
            offset = transformation.getComposite().getOffset()
            if offset.getAnimated() is not None:
                return offset.getAnimated().getWaypoint()
            elif offset.getVector() is not None:
                return offset.getVector()
        
        if name == "origin":
            origin = self.getParam("origin")
            if origin.getAnimated() is not None:
                return origin.getAnimated().getWaypoint()
            elif origin.getVector() is not None:
                return origin.getVector()

        if name == "scale":
            transformation = self.getParam("transformation")
            scale = transformation.getComposite().getScale()
            if scale.getAnimated() is not None:
                return scale.getAnimated().getWaypoint()
            elif scale.getVector() is not None:
                return scale.getVector()

        if name == "z_depth":
            z_depth = self.getParam("z_depth")
            if z_depth.getAnimated() is not None:
                return z_depth.getAnimated().getWaypoint()
            elif z_depth.getValue() is not None:
                return z_depth.getValue()

        if name == "amount":
            amount = self.getParam("amount")
            if amount.getAnimated() is not None:
                return amount.getAnimated().getWaypoint()
            elif amount.getValue() is not None:
                return amount.getValue()

    def getTagParam(self, pathTag):
        tmp = pathTag.split(".",1)
        paramRoot = tmp[0]
        tags = tmp[1].split(".")
        
        if paramRoot == "z_depth":
            pass
        elif paramRoot == "amount":
            pass
        elif paramRoot == "blend_method":
            pass
        elif paramRoot == "tranformation":
            if len(tags) == 1:
                if tags[0] == "composite":
                    return self.HashParam["transformation"].getComposite();
            elif len(tags) == 2:
                if tags[1] == "offset":
                    return self.HashParam["transformation"].getComposite().getOffset()
                elif tags[1] == "angle":
                    return self.HashParam["transformation"].getComposite().getAngle()
                elif tags[1] == "skew_angle":
                    return self.HashParam["transformation"].getComposite().getSkewAngle()
                elif tags[1] == "scale":
                    return self.HashParam["transformation"].getComposite().getScale()
            elif len(tags) == 3:    
                if tags[1] == "offset" and tags[2] == "animated":
                    return self.HashParam["transformation"].getComposite().getOffset().getAnimated()
