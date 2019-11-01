import numpy as np
from prettytable import PrettyTable

"""
Prompt
For the given geometry of an edge crack of length a (6mm or 30mm) find K_I
"""

"""GIVEN"""
w = 120  # mm
B = 10  # mm
a = np.array([6, 30])  # mm
P = 100  # kN

"""Unit Conversion [meters or Newtons]"""
w = w * 0.001
B = B * 0.001
a = a * 0.001
P = P * 1000

print(P)

"""Tension"""
print("Tension Component")
aw = a / w
print("A/W = ", aw)
Y_ten_1 = float(input("What is Y value for a = 6mm "))  # 2
Y_ten_2 = float(input("What is Y value for a = 30mm "))  # 2.5
Y_ten = np.array([Y_ten_1, Y_ten_2])
qq = (P * a**(1/2))/(B * w)
K_I_ten = Y_ten * qq
print("K_I_tension at 3mm", K_I_ten.item(0)*(10**-6))
print("")

"""Bending"""
print("Bending Component")
# Assuming pure bending
M = (40 * 0.001) * P
Y_ben_1 = float(input("What is the Y value for a = 6mm ")) # 1.9
Y_ben_2 = float(input("What is the Y value for a = 30mm ")) # 1.95
Y_ben = np.array([Y_ben_1, Y_ben_2])
num = 6 * M * a ** 0.5
dem = B * w **2
ee = num / dem
#ee = (6 * M * a ** (1/2))/(B * w)**2
K_I_ben = Y_ben * ee
print("K_I_bending at 3mm", K_I_ben.item(0)*(10**-6))
print("")

print("Troubleshooting")
print("M",M)
print("a",a)
print("B",B)
print("W",w)
print("ee", ee)

"""Superposition"""
K_I = K_I_ben + K_I_ten

K_I = K_I * (10**-6)

"""Table Output"""


print("")
tab = PrettyTable()
tab.field_names = ["Variable", "Value", "Units", "Value Type"]
tab.add_row(["a/W", aw, "dim", "Intermediate"])
tab.add_row(["K_I_ten", K_I_ten, "Pa*(M^0.5)", "Intermediate" ])
tab.add_row(["M", M, "N - m", "Intermediate"])
tab.add_row(["K_I_ben", K_I_ben, "Pa*(M^0.5)", "Intermediate"])
tab.add_row(["K_I", K_I,"MPa*(M^0.5)","Solution Array"])
tab.add_row(["K_I (a = 6mm)", round(K_I.item(0),1), "MPa*(M^0.5)", "SOLUTION"])
tab.add_row(["K_I (a = 30mm)", round(K_I.item(1),1), "MPa*(M^0.5)", "SOLUTION"])

print(tab)