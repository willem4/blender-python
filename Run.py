#script to run:
SCRIPT = "test_blender.py"  
    
#path to your org.python.pydev.debug* folder (it may have different version number, in your configuration):
PYDEVD_PATH='/Applications/eclipse/plugins/org.python.pydev_4.0.0.201504132356/pysrc/'
PYDEV_DEBUG_PATH='/Applications/Blender/'

import sys 
sys.path.append(PYDEV_DEBUG_PATH)

import pydev_debug as pydev

debugmode = False
pydev.debug(SCRIPT, PYDEVD_PATH, debugmode)
