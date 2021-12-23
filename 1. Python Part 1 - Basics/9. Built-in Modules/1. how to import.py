# module - python file
# package - multiple modules/files are contained in a folder
# Library - consist of multiple packages/folders

# import <module/package/library name>
import math

# import <package_name>
from json import decoder

# import <module/package name> as <alias name>
from json import decoder as jdecoder
# import math as m

print(dir())

# note - avoid polluting local space with unpacked packages or by using from keyword (use alias to avoid).
# see the difference in below example

import tkinter
print(dir())

from tkinter import *
print(dir())
