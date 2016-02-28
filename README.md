# pysynfig

###Introduction
pysynfig is a python package, a collection of modules, that could help you to create your own plugin for Synfig Studio.
You can find informations about how to create a plugin for synfig [here](http://wiki.synfig.org/Doc:Plugins).

So plugins let you to modify (at run time) from python script the .sif file.
To modify the sif file you must:

- **parse** .sif
- **modify** the tags of your interest in memory
- **write** the .sif on the disk

This operations, especially the parsing process, could be tedious and sure distract you from the resolution of the problem.

pysynfig offers you a simple api to parse the sif and to select/modify the tags of your interest, and finally write them on the disk. So you can spend your time to write the logic of the plugin without worrying about the process of parsing/modifying/writing.
It sounds as a good thing ;)

###Structure
pysynfig is a collection of module, the modules are located into these dirs:
- **objects**: here are located all the classes that represent the tags in the .sif
  - **params**: here are located all the classes for only the param tags in the sif
  - **tags**: here are located all the classes for all the restant tags in the sif that are not a param tag
- **reader**: here are located the classes to parse the .sif
- **interface**: here are located the classes that the the user (you) should use for parsing/modifying/writing the sif

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
At this moment the interface module is not yet implemented, so you must use the api of the sublevels (located in the objects/reader dirs). 
For example, suppose you have a .sif in which you have a layer (named empty) like in the text below, and you want:
- change **z_depth** from 0 to 1 (**raise up** the layer)
-  change **amount** from 0 to 1 (**show** the layer, amout==opacity)
-  change **scale** (**elimate the scaling**)
  - change x from 0.6170362830 to 1
  - change y from 0.6170362830 to 1

```xml
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
The code below show the functions you should use to complete the above tasks.
At this moment there is not a doc for the api, and it won't exist until the 
interface module will be completed. In general, the steps are:

- **STEP 1** parsing
- **STEP 2** selection of a layer
- **STEP 3** modification of the tags
  - you can get the param/tag with layer_object.getParam("param_or_tag_of_interest")
- **STEP 4** writing

When the interface module will be finisched these opeations will be more easy (i hope ^__^)
```python
#importing the class for parsing
from pysynfig.reader import XmlParser
#--------------STEP 1-----------------
#parse the file example.sif
parser = XmlParser("example.sif")
parser.parse()
parser.getLayers(parser.tree, parser.listLayer)

#--------------STEP 2-----------------
#get the list of the layers
#this a list of Layer objects 
#(Layer is a class in the objects/tags dir) 
list = p.getListLayers()
#select the layer of interest
#for example the first in the list (index 0)
zero = list[0]

#--------------STEP 3-----------------
#modify z_depth
z = zero.getParam("z_depth")
z.setValue("1.0000000000")

#modify amount
amount = zero.getParam("amount")
amount.setValue("1.0000000000")

#modify scale
transformation = zero.getParam("transformation")
composite = transformation.getComposite()
scale = composite.getScale()
scale.setVectorX("0.0000000000")
scale.setVectorY("0.0000000000")

#--------------STEP 4-----------------
#write the .sif 
parser.tree.write("prova.xml")
```

