Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path.append("C:\Data\Python_Library\MS")
>>> import MPS
>>> MPS.MPS(1, 20, 0, 0, 0, 1, 2, 3)
namespaces valid
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
  File "<pyshell#3>", line 1, in <module>
    MPS.MPS(1, 20, 0, 0, 0, 1, 2, 3)
  File "C:\Data\Python_Library\MS\MPS.py", line 125, in MPS
    coordinate_assign(new_coordinates, object_number)
  File "C:\Data\Python_Library\MS\MPS_base_functions.py", line 7, in coordinate_assign
    MPS.object_properties[index_numer + 0] = new_coordinates[0]
NameError: name 'index_numer' is not defined
>>> 
