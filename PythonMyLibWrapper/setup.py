

from setuptools import find_packages, setup, Extension

import ctypes
import pathlib
import os
import sys

import numpy as np

#from mylib_pkg import mylib_calc_wrapper 
#import mylib_pkg 

setup(
    name='MyCFuncWrapper',
    version="1.0",
    packages=['MyCFuncWrapper'], 
    # install_requires=[ 
    #     'numpy', 
    #     'sys',
    #     'pathlib',
    # ],
    include_package_data=True,
    package_data={'': ['MyLib.dll']}
)
