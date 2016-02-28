# pysynfig

###Introduction
pysynfig is a python package, a collection of modules, that could help you to create your own plugin for Synfig Studio.
You can find informations about how to create plugin for synfig [here](http://wiki.synfig.org/Doc:Plugins).

So plugins let you to modify (at run time) from python script the sif file.
To modify the sif file you must:

- to parse .sif
- to modify the tags of your interest in memory
- to write the .sif on the disk

This operations, especially the parsing process, could be tedious and sure distract you from the resolution of the problem.

pysynf offer you a simple api to parse the sif and to select/modify the tags of your interest, and finally write them on the disk. So you can spend your time to write the logic of the plugin without worrying about the process of parsing/modifying/writing.
It sounds as a good thing ;)

###Structure
pysynfig is a collection of module, the modules are located into theese dirs:
- objects: here are located all the class that represent the tags in the .sif
  - params: here are located all the class for only the param tags in the sif
  - tags: here are located all the class for all the restant tags in the sif that are not a param tag
- reader: here are located the class to parse the .sif
- interface: here are located the class the the user (you) should use for parsing/modifying/write the sif

You can use the tree list below as a reference for the implemented tag in pysynf.
If the tag you want to modify is present in the list, you can use pysynf's api for that.
This list grows up quickly, don't worry ;)
```
[kinder@localhost dev]$ tree pysynfig/
pysynfig/
├── __init__.py
├── __init__.pyc
├── objects
│   ├── __init__.py
│   ├── params
│   │   ├── __init__.py
│   │   ├── ParamBlendMethod.py
│   │   ├── ParamBr.py
│   │   ├── ParamCanvas.py
│   │   ├── ParamChildrenLock.py
│   │   ├── ParamColor.py
│   │   ├── ParamC.py
│   │   ├── ParamOrigin.py
│   │   ├── ParamPoint.py
│   │   ├── Param.py
│   │   ├── ParamTl.py
│   │   ├── ParamTransformation.py
│   └── tags
│       ├── Angle.py
│       ├── Animated.py
│       ├── Color.py
│       ├── Composite.py
│       ├── __init__.py
│       ├── Keyframe.py
│       ├── Layer.py
│       ├── MainCanvas.py
│       ├── Meta.py
│       ├── Offset.py
│       ├── Point.py
│       ├── Scale.py
│       ├── SkewAngle.py
│       ├── Vector.py
│       ├── Waypoint.py
│       
├── reader
│   ├── __init__.py
│   ├── XmlParser.py



```

###How to use
At this moment the interface module is not iyet mplemented, so you must use the api of the sublevels (located in the objects/reader dirs). 
For example, suppose you have a .sif in which you a are a layer (named empty) like in the text below, and you want:
- 1. change **z_depth** from 0 to 1 (**raise up** the layer)
- 2. change **amount** from 0 to 1 (**show** the layer, amout==opacity)
- 3. change **scale** (**elimate the scaling**)
  - change x from 0.6170362830 to 1
  - change y from 0.6170362830 to 1
- 4. change **angle** from 0 to 45 (**rotate** the layer)

```
 <layer type="switch" active="true" exclude_from_rendering="false" version="0.0" desc="empty.jpg">
    <param name="z_depth">
      <real value="0.0000000000"/>
    </param>
    <param name="amount">
      <real value="0.0000000000"/>
    </param>
    <param name="blend_method">
      <integer value="0" static="true"/>
    </param>
    <param name="origin">
      <vector>
        <x>0.0000000000</x>
        <y>0.0000000000</y>
      </vector>
    </param>
    <param name="transformation">
      <composite type="transformation">
        <offset>
          <vector>
            <x>0.0000000000</x>
            <y>0.0000000000</y>
          </vector>
        </offset>
        <angle>
          <angle value="0.000000"/>
        </angle>
        <skew_angle>
          <angle value="0.000000"/>
        </skew_angle>
        <scale>
          <vector>
            <x>0.6170362830</x>
            <y>0.6170362830</y>
          </vector>
        </scale>
      </composite>
    </param>

...
```
```
#importing the class for parsing
from pysynfig.reader import XmlParser

#parse the file example.sif
parser = XmlParser("example.sif")
parser.parse()
parser.getLayers(parser.tree, parser.listLayer)

#get the list of the layers
#this a list of Layer objects 
#(Layer is a class in the objects/tags dir) 
list = p.getListLayers()

#select the layer of interest
#for example the first in the list (index 0)
zero = list[0]

#modify z_depth
z = zero.getParam("z_depth")
z.setValue("1.0000000000")

#modify amount
amount = zero.getParam("amount")
amount.setValue("1.0000000000")

#modify angle

#modify scale
transformation = zero.getParam("transformation")
composite = transformation.getComposite()
scale = composite.getScale()
scale.setVectorX("0.0000000000")
scale.setVectorY("0.0000000000")

#write the .sif 
parser.tree.write("prova.xml")
```

