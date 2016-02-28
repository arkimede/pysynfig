# pysynfig

##Introduction
pysynfig is a python package, a collection of modules, that could help you to create your own plugin for Synfig Studio.
You can find informations about how to create plugin for synfig [here](http://wiki.synfig.org/Doc:Plugins).

So plugins let you to modify (at run time) from python script the sif file.
To modify the sif file you must:
1. __to parse__ sif file
2. __to modify__ the tags of your interest in memory
3. __to write__ the sif file on the disk

This operations, especially the parsing process, could be tedious and sure distract you from the resolution of the problem.

pysynf offer you a simple api to parse the sif and to select/modify the tags of your interest, and finally write them on the disk. So you can spend your time to write the logic of the plugin without worrying about the process of parsing/modifying/writing.
It sounds as a good thing ;)
