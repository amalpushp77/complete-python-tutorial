# https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c

# difference in ImportError and ModuleNotFound

# import maths
# this gives ModuleNotFoundError as no module with name maths have been found neither in local nor in python_home path

# from . import math
# this gives ImportError as nothing (package, module, class, function, variable) is present with the name maths
# in __main__ scope

from math import cosec
# this gives ImportError with the similar reason as above
