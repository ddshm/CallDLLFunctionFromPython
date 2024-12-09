
import ctypes
import numpy as np

from MyCFuncWrapper import mylib_calc_wrapper 


if __name__ == "__main__":
    print('Testing MyLib.dll')

    x = 1.5
    result = mylib_calc_wrapper.mylib_calc([2.0,2,2,2,2,2,2,2,2,2])
    print('result = ', result)

    # that cirrently does not work:
    
    arr3 = np.ndarray(shape = (10), dtype = ctypes.c_double) #;np.ascontiguousarray(0.0, dtype = ctypes.c_double)
    for i in range(10):
        arr3[i] = i + 0.1

    result2 = mylib_calc_wrapper.mylib_calc(arr3)
    print('result2 = ', result2)


