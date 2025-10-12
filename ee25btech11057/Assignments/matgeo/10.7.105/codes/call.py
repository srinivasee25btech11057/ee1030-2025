import os
import ctypes
import numpy as np  

so_path = os.path.abspath("parabola.so")



lib = ctypes.CDLL(so_path)

lib.main.restype = ctypes.c_int


result = lib.main()

print("C code executed successfully with return code:", result)


