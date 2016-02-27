from xml.etree import ElementTree
from pysynfig.objects.tags import Layer 
from pysynfig.objects.params import Param 
from pysynfig.objects.params import ParamBlendMethod
from pysynfig.objects.params import ParamOrigin
from pysynfig.objects.params import ParamColor
from pysynfig.objects.params import ParamPoint
from pysynfig.objects.tags import Color
from pysynfig.objects.params import ParamTransformation
from pysynfig.objects.tags import Offset
from pysynfig.objects.tags import Animated
from pysynfig.objects.tags import Waypoint
from pysynfig.objects.tags import Vector
from pysynfig.objects.tags import Point
from pysynfig.objects.tags import Angle
from pysynfig.objects.tags import SkewAngle
from pysynfig.objects.tags import Composite
from pysynfig.objects.params import ParamChildrenLock
from pysynfig.objects.params import ParamCanvas
from pysynfig.objects.params import ParamTl
from pysynfig.objects.params import ParamBr
from pysynfig.objects.params import ParamC
from pysynfig.objects.tags import Scale
from pysynfig.objects.tags import MainCanvas
from pysynfig.objects.tags import Meta
from pysynfig.objects.tags import Keyframe
#import pdb

class XmlParser:

    def __init__(self,filename):
        self.filename = filename
        self.tree = None
        self.listLayer = []
        self.mainCanvas = None
        self.maxZ = 0

    def parse(self):
        with open(self.filename, 'rt') as f:
                self.tree = ElementTree.parse(f)
        return self.tree


    def printXml(self):
        for node in self.tree.iter():
            print(node.tag, node.attrib, node.text)

    def getListLayers(self):
        return self.listLayer

    def getMainCanvas(self,startNode):
            #root = startNode.findall('./canvas')[0]
            for index, tag in enumerate(self.tree.iter()):
                if index == 0 and tag.tag == "canvas":
                    root = tag
                    break
                
            tmpCanvas = MainCanvas()
            #parsing degli attributi del tag canvas
            idAttrib = root.attrib.get('id')
            if idAttrib is not None:
                tmpCanvas.setId(idAttrib)
            guidAttrib = root.attrib.get('guid')
            if guidAttrib is not None:
                tmpCanvas.setGuid(guidAttrib)
            versionAttrib = root.attrib.get('version')
            if versionAttrib is not None:
                tmpCanvas.setVersion(versionAttrib)
            widthAttrib = root.attrib.get('width')
            if widthAttrib is not None:
                tmpCanvas.setWidth(widthAttrib)
            heightAttrib = root.attrib.get('height')
            if heightAttrib is not None:
                tmpCanvas.setHeight(heightAttrib)
            xresAttrib = root.attrib.get('xres')
            if xresAttrib is not None:
                tmpCanvas.setXres(xresAttrib)
            yresAttrib = root.attrib.get('yres')
            if yresAttrib is not None:
                tmpCanvas.setYres(yresAttrib)
            fpsAttrib = root.attrib.get('fps')
            if fpsAttrib is not None:
                tmpCanvas.setFps(fpsAttrib)
            startTimeAttrib = root.attrib.get('start_time')
            if startTimeAttrib is not None:
                tmpCanvas.setStartTime(startTimeAttrib)
            beginTimeAttrib = root.attrib.get('begin_time')
            if beginTimeAttrib is not None:
                tmpCanvas.setBeginTime(beginTimeAttrib)
            endTimeAttrib = root.attrib.get('end_time')
            if endTimeAttrib is not None:
                tmpCanvas.setEndTime(endTimeAttrib)
            antialiasAttrib = root.attrib.get('antialias')
            if antialiasAttrib is not None:
                tmpCanvas.setAntialias(antialiasAttrib)
            viewBoxAttrib = root.attrib.get('view_bow')
            if viewBoxAttrib is  not None:
                tmpCanvas.setViewBox(viewBoxAttrib)
            bgColorAttrib = root.attrib.get('bg_color')
            if bgColorAttrib is not None:
                tmpCanvas.setBgColor(bgColorAttrib)
            focusAttrib = root.attrib.get('focus')
            if focusAttrib is not None:
                tmpCanvas.setFocus(focusAttrib)

            #parsing tag name
            #pdb.set_trace()
            name = root.findall('name')[0]
            NameValue = name.text
            tmpCanvas.setName(NameValue)
            #parsing tags meta
            tmpListMeta = []
            for meta in root.findall('meta'):
                tmpMeta = Meta()
                paramName = meta.attrib.get('name')
                tmpMeta.setName(paramName)
                paramContent = meta.attrib.get('content')
                tmpMeta.setContent(paramContent)
                tmpListMeta.append(tmpMeta)
            tmpCanvas.setMeta(tmpListMeta)

            #parsing tag keyframe
            keyframe = root.findall('keyframe')[0]
            tmpKeyframe = Keyframe()
            time = keyframe.attrib.get('time')
            tmpKeyframe.setTime(time)
            active = keyframe.attrib.get('active')
            tmpKeyframe.setActive(active)
            tmpCanvas.setKeyframe(tmpKeyframe)
            
            self.mainCanvas = tmpCanvas

    def getLayers(self, startNode, list):
        numLayer = len(startNode.findall('layer'))

        for node in startNode.findall('layer'):

            tmpLayer = Layer()
	    tmpLayer.setNode(node)
	    #parsing degli attributi del layer
            typeAttrib = node.attrib.get('type')
            if typeAttrib:
                tmpLayer.setType(typeAttrib)
                self.printInfo('type',typeAttrib)
            
            activeAttrib = node.attrib.get('active')
            if activeAttrib:
                tmpLayer.setActive(activeAttrib)
                self.printInfo('active',activeAttrib)

            efrAttrib = node.attrib.get('exclude_from_rendering')
            if efrAttrib:
                tmpLayer.setExcludeFromRendering(efrAttrib)
                self.printInfo('exclude_from_rendering',efrAttrib)

            descAttrib = node.attrib.get('desc')
            if descAttrib:
                tmpLayer.setDesc(descAttrib)
                self.printInfo('desc',descAttrib)

            #parsing dei param del layer

            for param in node.findall('param'):
                paramName = param.get('name')
                self.parseParamLayer(paramName, param, tmpLayer)
                #rank = params.find('rank').text
                #name = params.get('name')
                #print name, rank

            #insert layer into the list
            list.append(tmpLayer)

    def parseParamLayer(self, paramName, param, parentLayer):
        if paramName == "z_depth":
            self.parseZdepth(param, parentLayer)
        elif paramName == "amount":
            self.parseAmount(param, parentLayer)
        elif paramName == "blend_method":
            self.parseBlendMethod(param, parentLayer)
        elif paramName == "origin":
            self.parseOrigin(param, parentLayer)
        elif paramName == "transformation":
            self.parseTransformation(param, parentLayer)
        elif paramName == "canvas":
            self.parseCanvas(param, parentLayer)
        elif paramName == "time_dilatation":
            self.parseTimeDilation(param, parentLayer)
        elif paramName == "time_offset":
            self.parseTimeOffset(param, parentLayer)
        elif paramName == "children_lock":
            self.parseChildrenLock(param, parentLayer)
        elif paramName == "outline_grow":
            self.parseOutlineGrow(param, parentLayer)
        elif paramName == "layer_name":
            self.parseLayerName(param, parentLayer)
        elif paramName == "tl":
            self.parseLayerName(param, parentLayer)
        elif paramName == "br":
            self.parseLayerName(param, parentLayer)
        elif paramName == "c":
            self.parseLayerName(param, parentLayer)
        elif paramName == "gamma_adjust":
            self.parseLayerName(param, parentLayer)
        elif paramName == "filename":
            self.parseLayerName(param, parentLayer)
        elif paramName == "delay":
            self.parseDelay(param, parentLayer)
        elif paramName == "volume":
            self.parseVolume(param, parentLayer)
        elif paramName == "color":
            self.parseColor(param, parentLayer)
        elif paramName == "point1":
            self.parsePoint(param, parentLayer)
        elif paramName == "point2":
            self.parsePoint(param, parentLayer)
        elif paramName == "expand":
            self.parseExpand(param, parentLayer)
        elif paramName == "invert":
            self.parseInvert(param, parentLayer)


    def parseZdepth(self, param, parentLayer):
        tmpParam = Param()

        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)

        #tag animated
        #<param name="z_depth">
        #<animated type="real">
        #  <waypoint time="0s" before="constant" after="constant">
        #    <real guid="26975B3DE485F8BA47FEA3264ED12535" value="4.0000000000"/>
        #  </waypoint>
        #  <waypoint time="2.75s" before="constant" after="constant">
        #    <real guid="0491D9C9521E82CAD85C27CE4FCC1643" value="0.0000000000"/>
        # </waypoint>
        #</animated>
        #</param>
        animated = param.find('animated')
        if animated is not None:
            tmpAnimated = self.parseAnimated(animated)
            tmpParam.setAnimated(tmpAnimated)
        #<param name="z_depth">
            #  <real value="0.0000000000"/>
        #</param>
        else:
            #seleziono il tag real
            real = param.find('real')
            #prendo il l'attributo value del tag real
            if real is not None:
                value = real.get('value')
		tmpParam.setNode(real)
                tmpParam.setValue(value)
                self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseAmount(self, param, parentLayer):
        #pdb.set_trace()
        tmpParam = Param()
        #<param name="amount">
            #  <real value="0.0000000000"/>
        #</param>
        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        #tag animated
        #<param name="amount">
        #  <animated type="real">
        #    <waypoint time="0s" before="clamped" after="clamped">
        #      <real guid="1A7568D8708996425BD1F8B7B7DB6933" value="1.0000000000"/>
        #    </waypoint>
        #    <waypoint time="1.54166663s" before="clamped" after="clamped">
        #      <real guid="1003403B8E4A99E385EC86C414CC569A" value="0.0000000000"/>
        #    </waypoint>
        #  </animated>
        #</param>
        animated = param.find('animated')
        if animated is not None:
            tmpAnimated = self.parseAnimated(animated)
            tmpParam.setAnimated(tmpAnimated)
        else:
            #seleziono il tag real
            real = param.find('real')
            #prendo l'attributo value del tag real
            if real is not None:
                value = real.get('value')
		tmpParam.setNode(real)
                tmpParam.setValue(value)
                self.printInfo('value',value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseBlendMethod(self, param, parentLayer):
        tmpParam = ParamBlendMethod()
        #<param name="blend_method">
            #<integer value="0" static="true"/>
            #</param>
        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)
        #seleziono il tag integer
        integer = param.find('integer')
        #prendo l'attributo value del tag integer
        if integer is not None:
            value = integer.get('value')
	    tmpParam.setNode(integer)
            tmpParam.setValue(value)
            self.printInfo('value',value)

            static = integer.get('static')
            tmpParam.setStatic(static)
            if static is not None:
                self.printInfo('static', static)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseOrigin(self, param, parentLayer):
        tmpParam = ParamOrigin()
	name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        #tag animated
        animated = param.find('animated')
        if animated is not None:
            tmpAnimated = self.parseAnimated(animated)
            tmpParam.setAnimated(tmpAnimated)

        #<param name="origin">
        #  <vector>
            #    <x>0.0000000000</x>
            #    <y>0.0000000000</y>
            #  </vector>
            #</param>
        #seleziono il tag vector
        else:
            vector = param.find('vector')
	    
            if vector is not None:
                x = vector.find('x').text
                y = vector.find('y').text
                tmpParam.setVector(x,y,vector)
                self.printInfo('x',x)
                self.printInfo('y',y)

        #aggiungo il param all'hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseColor(self, param, parentLayer):
        tmpParam = ParamColor()
        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        """
        <param name="color">
            <color>
                <r>1.000000</r>
                <g>1.000000</g>
                <b>1.000000</b>
                <a>1.000000</a>
            </color>
        </param>
        """

        color = param.find('color')
        if color is not None:
            r = color.find('r').text
            g = color.find('g').text
            b = color.find('b').text
            a = color.find('a').text
            tmpColor = Color(r, g, b, a)
            tmpParam.setColor(tmpColor)

        #aggiungo il param all'hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parsePoint(self, param, parentLayer):
        tmpParam = ParamPoint()
        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        """
        <param name="point1">
            <vector>
                <x>-2.9333333969</x>
                <y>1.5333333015</y>
            </vector>
        </param>
        """
        #seleziono il tag vector
        vector = param.find('vector')
        if vector is not None:
            x = vector.find('x').text
            y = vector.find('y').text
            tmpParam.setPoint(Point(Vector(x, y)))
            self.printInfo('x',x)
            self.printInfo('y',y)

        #aggiungo il param all'hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseExpand(self, param, parentLayer):
        #pdb.set_trace()
        tmpParam = Param()

        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        """
        <param name="expand">
            <real value="0.0000000000"/>
        </param>
        """
        #seleziono il tag real
        real = param.find('real')
        #prendo l'attributo value del tag real
        if real is not None:
            value = real.get('value')
            tmpParam.setNode(real)
            tmpParam.setValue(value)
            self.printInfo('value',value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseInvert(self, param, parentLayer):
        #pdb.set_trace()
        tmpParam = Param()

        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        """
        <param name="invert">
            <bool value="false"/>
        </param>
        """
        #seleziono il tag real
        bool = param.find('bool')
        #prendo l'attributo value del tag bool
        if bool is not None:
            value = bool.get('value')
            value = (value is True)
            tmpParam.setBool(value)
            self.printInfo('value',str(value))
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseTransformation(self, param, parentLayer):  
        tmpParam = ParamTransformation()
        
        name = param.get('name')
        self.printInfo('name',name)
        tmpParam.setName(name)

        #tag composite
        composite = param.find('composite')
        tmpComposite = self.parseComposite(composite, parentLayer)
        tmpParam.setComposite(tmpComposite)
        #aggiungo il param all'hash
        parentLayer.addParam(tmpParam)
           
    def parseComposite(self, composite, parentLayer):
        tmpComposite = Composite()
        #param type
        paramType = composite.get('type')
        tmpComposite.setType(paramType)

        #tag offset
        offset = composite.find('offset')
        tmpOffset = self.parseOffset(offset, parentLayer)
        tmpComposite.setOffset(tmpOffset)
        
        #tag angle
        angle = composite.find('angle')
        tmpAngle = self.parseAngle(angle,parentLayer)
        tmpComposite.setAngle(tmpAngle)

        #tag skew_angle
        skew_angle = composite.find('skew_angle')
        tmpSkewAngle = self.parseSkewAngle(skew_angle, parentLayer)
        tmpComposite.setSkewAngle(tmpSkewAngle)

        #tag scale
        scale = composite.find('scale')
        tmpScale = self.parseScale(scale, parentLayer)
        tmpComposite.setScale(tmpScale)
        return tmpComposite

    def parseTimeOffset(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag time
        time = param.find('time')
        #prendo il l'attributo value del tag real
        if time is not None:
            value = time.get('value')
	    tmpParam.setNode(time)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseCanvas(self, param, parentLayer):
        #pdb.set_trace()
        tmpParamCanvas = ParamCanvas()
        name = param.get('name')
        tmpParamCanvas.setName(name)
        self.getLayers(param.find('canvas'), tmpParamCanvas.getLayers())
        self.setFilenameParamImportLayer(tmpParamCanvas, parentLayer)
        parentLayer.addParam(tmpParamCanvas)

    def setFilenameParamImportLayer(self, paramCanvas, parentLayer):
        layers = paramCanvas.getLayers()
        for layer in layers:
            layerType = layer.getType()
            if layerType == 'import':
                #print("nome fileeeeee")
                param = layer.HashParam['filename']
                tmpParam = Param()
                tmpParam.setName(param.getName())
                tmpParam.setText(param.getText())
                #git add print("nom del file: " + tmpParam.getText())
                parentLayer.setFilenameParamImportLayer(tmpParam)
                break

    def parseTimeDilation(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag real
        real = param.find('real')
        #prendo il l'attributo value del tag real
        if real is not None:
            value = real.get('value')
            tmpParam.setNode(real)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseChildrenLock(self, param, parentLayer):
        tmpParam = ParamChildrenLock()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag bool
        bool = param.find('bool')
        #prendo gli attributi value  e static del tag bool
        if bool is not None:
            value = bool.get('value')
            static = bool.get('static')
            if value is not None:
                tmpParam.setNode(bool)
                tmpParam.setValue(value)
                self.printInfo('value', value)
            if static is not None:
                tmpParam.setStatic(static)
                self.printInfo('static', static)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseOffset(self, offset, parentLayer):
        tmpOffset = Offset()
        #tag animated
        animated = offset.find('animated')
        if animated is not None:
            tmpAnimated = self.parseAnimated(animated)
            tmpOffset.setAnimated(tmpAnimated)
        #tag vector
        vector = offset.find('vector')
        if vector is not None:
            tmpVector = self.parseVector(vector)
            tmpOffset.setVector(tmpVector)
        return tmpOffset

    def parseAngle(self,angle,parentLayer):
        tmpAngle = Angle()
        animated = angle.find('animated')
        if animated is not None:
            """
            <angle>
                <animated type="angle">
                    <waypoint time="0s" before="clamped" after="clamped">
                        <angle guid="7048314E0FD2E14C2D18511C7DBF27FB" value="0.000000"/>
                    </waypoint>
                    <waypoint time="1s" before="clamped" after="clamped">
                        <angle guid="C7D4CA1E22F3A49C04F66B8E44A7B6E6" value="-42.825256"/>
                    </waypoint>
                </animated>
            </angle>
            """
            tmpAnimated = self.parseAnimated(animated)
            tmpAngle.setAnimated(tmpAnimated)
        else:
            """
            <angle>
                <angle value="-31.675468"/>
            </angle>
            """
	    angle_ = angle.find('angle')
            angleValue = angle_.get('value')
            tmpAngle.setValue(angleValue)
        return tmpAngle

    def parseSkewAngle(self, skew_angle,parentLayer):
        #tag skew_angle
        tmpSkewAngle = SkewAngle()
        angle_ =  skew_angle.find('angle')
	skewAngleValue = angle_.get('value')
        tmpSkewAngle.setValue(skewAngleValue)
        return tmpSkewAngle

    def parseDelay(self, param, parentLayer):
        tmpParam = Param()

        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)

        """
        <param name="delay">
            <time value="0s" static="true"/>
        </param>
        """
        #seleziono il tag time
        time = param.find('time')
        #prendo il l'attributo value del tag real
        if time is not None:
            value = time.get('value')
            tmpParam.setNode(time)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseVolume(self, param, parentLayer):
        tmpParam = Param()

        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)

        """
        <param name="volume">
            <real value="1.0000000000" static="true"/>
        </param>
        """
        #seleziono il tag time
        real = param.find('real')
        #prendo il l'attributo value del tag real
        if real is not None:
            value = real.get('value')
            tmpParam.setNode(real)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)
    
    def parseScale(self, scale,parentLayer):
        tmpScale = Scale()
        #tag vector
        vector = scale.find('vector')
        if vector is not None:
            tmpVector = self.parseVector(vector)
            tmpScale.setVector(tmpVector)
        #tag scale
        animated = scale.find('animated')
        if animated is not None:
            tmpAnimated = self.parseAnimated(animated)
            tmpScale.setAnimated(tmpAnimated)
        
        return tmpScale
    
    def parseAnimated(self, animated):  
        tmpAnimated = Animated()
        #param type
        paramType = animated.get('type')
        tmpAnimated.setType(paramType)

        #tutti i tag waypoint
        waypointList = animated.findall('waypoint')
        for waypoint in waypointList:
            tmpWaypoint = self.parseWaypoint(waypoint, paramType)
            tmpAnimated.addWaypoint(tmpWaypoint)
        return tmpAnimated

    def parseWaypoint(self, waypoint, parentType):
        #pdb.set_trace()
        tmpWaypoint = Waypoint()
        #parametri: time, before, after
        time = waypoint.get('time')
        #in z_depth inserisce time=-0s sostituisco con time=0s
        time = time.replace("-","")
        before = waypoint.get('before')
        after = waypoint.get('after')

        tmpWaypoint.setTime(time)
        tmpWaypoint.setBefore(before)
        tmpWaypoint.setAfter(after)

        tmpWaypoint.setParentType(parentType)

        #tag vector
        vector = waypoint.find('vector')
        if vector is not None:
            tmpVector = self.parseVector(vector)
            tmpWaypoint.setVector(tmpVector)
        #tag value
        real = waypoint.find('real')
        if real is not None:
            value = real.get('value')
            tmpWaypoint.setValue(value)
        #tag angle
        angle = waypoint.find('angle')
        if angle is not None:
            value = angle.get('value')
            tmpWaypoint.setValue(value)

        return tmpWaypoint
    
    def parseVector(self,vector):      
        x = vector.find('x').text
        y = vector.find('y').text
        tmpVector = Vector(x,y,vector)
        return tmpVector

    def parseOutlineGrow(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag real
        real = param.find('real')
        #prendo il l'attributo value del tag real
        if real is not None:
            value = real.get('value')
            tmpParam.setNode(real)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseLayerName(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag string
        string = param.find('string')
        #prendo il contenuto di string
        if string is not None:
            text = string.text
            tmpParam.setText(text)
            self.printInfo('string', text)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseTl(self, param, parentLayer):
        tmpParam = ParamTl()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag vector
        vector = param.find('vector')
        #prendo il contenuto di vector
        if vector is not None:
            x = vector.find('x').text
            y = vector.find('y').text
            objVector = Vector(x,y)
            tmpParam.setVector(objVector)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseBr(self, param, parentLayer):
        tmpParam = ParamBr()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag vector
        vector = param.find('vector')
        #prendo il contenuto di vector
        if vector is not None:
            x = vector.find('x').text
            y = vector.find('y').text
            objVector = Vector(x,y)
            tmpParam.setVector(objVector)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseC(self, param, parentLayer):
        tmpParam = ParamC()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag bool
        bool = param.find('bool')
        #prendo gli attributi value  e static del tag bool
        if bool is not None:
            value = bool.get('value')
            static = bool.get('static')
            tmpParam.setNode(bool)
            tmpParam.setValue(value)
            tmpParam.setStatic(static)
            self.printInfo('value', value)
            self.printInfo('static', static)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseGammaAdjust(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag real
        real = param.find('real')
        #prendo il l'attributo value del tag real
        if real is not None:
            value = real.get('value')
            tmpParam.setNode(real)
            tmpParam.setValue(value)
            self.printInfo('value', value)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def parseFilename(self, param, parentLayer):
        tmpParam = Param()
        name = param.get('name')
        self.printInfo('param',name)
        tmpParam.setName(name)
        #seleziono il tag string
        string = param.find('string')
        #prendo il contenuto di string
        if string is not None:
            text = string.text
            tmpParam.setText(text)
            self.printInfo('string', text)
        #aggiungo il param all hash dei param del layer
        parentLayer.addParam(tmpParam)

    def setMaxZ(self,list_):
        #pdb.set_trace()
        for l in list_:
            tmp = l.get("z_depth")
            if type(tmp) is list:
                tmp = float(tmp[0].getValue())
            else:
                tmp = float(tmp)

            if tmp > self.maxZ:
                self.maxZ = tmp

        for l in list_:
            l.setZmax(self.maxZ)


    def getMaxZ(self):
        if self.maxZ == None:
            self.setMaxZ()
        return self.maxZ

    def printInfo(self, name, value):
        print(name  + " = " + value)

    def printParsing(self):
        paramList = []
        for layer in self.listLayer:
            keys = layer.HashParam.keys()
            for keyname in keys:
                value = layer.HashParam[keyname]
                #print("DDDDD key = " + keyname + ", value.getName() = " + value.getName())
                paramList.append(value)
            """
            z_depth = layer.HashParam["z_depth"]
            amount = layer.HashParam["amount"]
            blend_method = layer.HashParam["blend_method"]
            origin = layer.HashParam["origin"]
            transformation = layer.HashParam["transformation"]
            paramList.append(z_depth)
            paramList.append(amount)
            paramList.append(blend_method)
            paramList.append(origin)
            paramList.append(transformation)
            """
            xml = ""
            for param in paramList:
                if param.getName() == "z_depth":
                    xml = xml + param.printXML()
                elif param.getName() == "amount":
                    xml = xml + param.printXML()
                elif param.getName() == "blend_method":
                    xml = xml + param.printXML()
                #elif param.getName() == "origin":
                   # xml = xml + param.printXML()
                elif param.getName() == "transformation":
                    xml = xml + param.printXML()
                elif param.getName() == "color":
                    xml = xml + param.printXML()
                elif param.getName() == "point1":
                    xml = xml + param.printXML()
                elif param.getName() == "point2":
                    xml = xml + param.printXML()
        return xml
