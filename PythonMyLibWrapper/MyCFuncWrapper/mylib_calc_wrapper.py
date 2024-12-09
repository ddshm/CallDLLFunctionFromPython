
import ctypes
import pathlib
import os
import sys

import numpy as np

dir_ = os.path.dirname(sys.modules['MyCFuncWrapper'].__file__)
print('MyCFuncWrapper dir = ', dir_)
libpathname = os.path.join(dir_, 'MyLib.dll')
print('MyCFuncWrapper libpathname = ', libpathname)

#libpathname = "MyLib.dll"
c_lib = ctypes.CDLL(libpathname)
mylib_calc_fn = c_lib.calculate
mylib_calc_fn.restype = ctypes.c_double

def mylib_calc(d):
    if isinstance(d, np.ndarray) and d.dtype == np.float64 and len(d.shape)==1:
        # THIS PART DOES NOT WORK!
        # it's already a numpy array with the right features - go zero-copy
        #a = d.ctypes.data
        a = d.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    else:
        # it's a list or something else - try to create a copy
        arr_t = ctypes.c_double * len(d)
        a = arr_t(*d)
    x = ctypes.c_double(1.5) # need to declare type if not int
    #x = 1.5
    res = ctypes.c_double
    len_ = len(d)
    res = mylib_calc_fn(x, a, len_)
    return res
