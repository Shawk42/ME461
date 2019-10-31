import numpy as np
from prettytable import PrettyTable

"""
Prompt
For the given geometry of an edge crack of length a (6mm or 30mm) find K_I
"""

"""GIVEN"""
w = 120  # mm
B = 10  # mm
a = 6  # mm
P = 100  # kN

"""Unit Conversion [meters or Newtons]"""
w = w * 0.001
B = B * 0.001
a = a * 0.001
P = P * 1000

"""Tension"""
aw = a / w
print("A/W = ", aw)
Y_ten = float(input("What is Y value for a = 6mm "))  # 2
qq = (P * a**(1/2))/(B * w)
K_I_ten = Y_ten * qq

"""Bending"""



"""Table Output"""
print("")
tab = PrettyTable()
tab.field_names = ["Variable", "Value", "Units", "Value Type"]
tab.add_row(["a/W", aw, "dim", "Intermediate"])
tab.add_row(["K_I_ten", K_I_ten, "UNITS", "Intermediate" ])

print(tab)