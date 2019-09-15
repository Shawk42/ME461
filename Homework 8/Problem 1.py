import numpy as np
from prettytable import PrettyTable

""" Givens """
# Material A
#Su = 500  # Mpa
#d = 5  # mm

# Material B
Su = 100  # ksi
d = 2  #in


Nf = 10**6

""" Table Values"""
# Material A
#Ksize = 1
#Kload = 0.8
#Ksurf = 0.6

# Material B
Ksize = 0.8  # Max modification is 0.8 @ 50 mm (2 in = 50.8mm)
Kload = 1
Ksurf = 0.9

""" Intermediate Calculations """
Sf_unmod = 0.5*Su

""" Solution Calculations """
Sf = Ksize * Kload * Ksurf * Sf_unmod
A = Su
B = np.log10(Sf / A)/np.log10(Nf)

"""Verification"""
Sf_check = A*(Nf**B)

""" Intermediate Outputs """
inter = PrettyTable(["Variable", "Value", "Units"])
inter.add_row(["Nf", Nf, "Cycles"])
inter.add_row(["Sf (Unmodified)", Sf_unmod, "Mpa"])
inter.add_row(["Sf (Verification)", Sf_check, ""])
print(inter)
print("")

"""Solution"""
sol = PrettyTable(["Material","Variable", "Value", "Units"])
sol.add_row(["A", "Sf", 120, "MPa"])
sol.add_row(["A","A", 500, "MPa"])
sol.add_row(["A","B", -0.1, ""])
sol.add_row(["B", "Sf", 36, "ksi"])
sol.add_row(["B","A", 100, "ksi"])
sol.add_row(["B","B", -0.07, ""])
sol.add_row(["C", "Sf", Sf, ""])
sol.add_row(["C","A", A, ""])
sol.add_row(["C","B", B, ""])
print(sol)
print("")


