import numpy as np
from prettytable import PrettyTable

""" Givens """
Su = 500  # Mpa
d = 5  # mm
Nf = 10**6

""" Table Values"""


""" Intermediate Calculations """
Sf_unmod = 0.5*Su

""" Solution Calculations """


""" Intermediate Outputs """
inter = PrettyTable(["Variable", "Value", "Units"])
inter.add_row(["Nf", Nf, "Cycles"])
inter.add_row(["Sf (Unmodified)", Sf_unmod, "Mpa"])
print(inter)
print("")

"""Solution"""
sol = PrettyTable(["Variable", "Value", "Units"])
sol.add_row(["Sf", "", ""])
sol.add_row(["A", Su, "MPa"])
sol.add_row(["B", "", ""])
print(sol)
print("")


