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
- interface

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

