1.
Build MyLib project. That should create x64\Release\MyLib.dll

2.
Build MyLibTestApp (static linkage) and MyLibTestApp2 (dynamic linkage) projects and test MyLib.DLL from C++ code

3.
Copy MyLib.dll from x64\Release folder into PythonMyLibWrapper\MyCFuncWrapper

Create a distribution of the package by running setup.py in the wrapper folder:
>cd U:\_Development\PythonCTypes2\PythonMyLibWrapper
>python setup.py sdist bdist_wheel

That should create mycfuncwrapper-1.0.tar.gz

4.
Install the package with the following command:
>pip install mycfuncwrapper-1.0.tar.gz

5.
Run PythonCFuncTest python test project
