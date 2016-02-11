Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path.append("C:\Data\Python_Library\MS")
>>> import MS
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import MS
ImportError: No module named 'MS'
>>> import MPS
>>> MPS.MPS(1, 20, 0, 0, 0, 1, 2, 3)
X_POS VALID!
Y_POS VALID!
Z_POS VALID!
X_MOVEMENT VALID!
Y_MOVEMENT VALID!
Z_MOVEMENT VALID!
X_ROT VALID!
Y_ROT VALID!
Z_ROT VALID!
CW VALID!
M VALID!
DENSITY VALID!
DIAMETER_X VALID!
DIAMETER_Y VALID!
DIAMETER_Z VALID!
METAL VALID!
STATE VALID!
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
All the parameters are valid
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    MPS.MPS(1, 20, 0, 0, 0, 1, 2, 3)
  File "C:\Data\Python_Library\MS\MPS.py", line 116, in MPS
    new_coordinates = lin_mov(object_number)
  File "C:\Data\Python_Library\MS\MPS_modules.py", line 4, in lin_mov
    print(test_namespaces)
NameError: name 'test_namespaces' is not defined
>>> #result namespaces not valid
>>> 
