"""
Program: Project2 Crase
Author: Cale Crase
Right Triangle Detector
"""

import math
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
if x > z and y > z:
    print("That is not a Right Triangle!")
else:
    print("That is a Right Triangle!")
