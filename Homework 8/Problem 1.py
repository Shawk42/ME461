import numpy as np
import numpy.random as rand
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from scipy import stats

""" Givens """
# Material A
Su = 500  # Mpa
d = 5  # mm

# Material B
#Su = 100  # ksi
#d = 2  #in

# Material C
#Su = 280  # ksi
#d = 0.25  #in

# Material D
#Su = 900  # MPa
#d = 10  #mm

Nf = 10**6

""" Table Values"""
# Material A - axial
Ksize = 1
Kload = 0.8
Ksurf = 0.6

# Material B - rotating bending
#Ksize = 0.7
#Kload = 1
#Ksurf = 0.9

# Material C - axial
#Ksize = 1
#Kload = 0.8
#Ksurf = 0.15

# Material D - rotating bending
#Ksize = 1  #As d = 10mm and the cutoff is 10mm, the size factor is being treated as 1
#Kload = 1
#Ksurf = 0.9

""" Intermediate Calculations """
Sf_unmod = 0.5*Su
#Sf_unmod = 100  # For Material C only due to Su > 200 ksi

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
# print("Intermediate Outputs")
# print(inter)
# print("")

"""Solution"""
sol = PrettyTable(["Material","Variable", "Value", "Units"])
sol.add_row(["A", "Sf", 120, "MPa"])
sol.add_row(["A","A", 500, "MPa"])
sol.add_row(["A","B", -0.1, ""])

sol.add_row(["B", "Sf", 31, "ksi"])
sol.add_row(["B","A", 100, "ksi"])
sol.add_row(["B","B", -0.08, ""])

sol.add_row(["C", "Sf", 12, "ksi"])
sol.add_row(["C","A", 280, "ksi"])
sol.add_row(["C","B", -0.22, ""])

sol.add_row(["D", "Sf", 405, "MPa"])
sol.add_row(["D","A", 900, "MPa"])
sol.add_row(["D","B", -0.05, ""])
print("Solution Values")
print(sol)
print("")

"""Live Linked Table"""
livelink = PrettyTable(["Material","Variable", "Value", "Units"])
livelink.add_row(["", "Sf", Sf, ""])
livelink.add_row(["","A", A, ""])
livelink.add_row(["","B", B, ""])
#print("Live Output")
#print(livelink)

"""Coefficent Table"""
coeff = PrettyTable(["Material","Su","d","Ksize","Kload","Ksurf"])
coeff.add_row(["A","500","5",1,0.8,0.6])
coeff.add_row(["B","100","2",0.8,1,0.9])
coeff.add_row(["C","20","0.25",1,0.8,0.15])
coeff.add_row(["D","500","5",1,1,0.9])

print("Table of coefficents used")
print(coeff)


"""
Monte Carlo Simulation

I am curious into the results of varying the range of acceptable values in this equation.
Material A will be used for these simulations

Kload will vary uniformly between 0.7 and 0.8
Ksurf will vary with a triangular distributimongon centered at 0.6, lower bound of 0.55, upper bound of 0.65
"""

Ksize = np.ones(250)
Kload = rand.uniform(0.7,0.8,250)
Ksurf = rand.triangular(0.55, 0.6, 0.65, 250)

Sf = Ksize * Kload * Ksurf * Sf_unmod

Sf_mean = round(np.mean(Sf), 2)
Sf_std = round(np.std(Sf), 2)
Sf_CI = stats.norm.interval(0.95,loc = Sf_mean, scale = Sf_std)

print("")
print("Monte Carlo Simulation Output")
print("Mean", Sf_mean)
print("Standard Deviation",Sf_std)
print("Confidence Interval",Sf_CI)


plt.hist(Sf, rwidth= 0.8, align= 'mid')
plt.xlabel("Sf [MPa]")
plt.ylabel("Count")
plt.show()

"""
Results 

A rough result of the Monte Carlo simulation shows that the resulting distribution is normal.
The unverified 95% confidence interval is 100 to 123, which contains the orginal solution.
"""




