import numpy as np
from prettytable import PrettyTable

"""Constants"""
sigma_f_prime = 807 * (10**6)
b = -0.071
c = -0.65
epsilon_f_prime = 0.86
E = 207 * (10**9)

"""Array Constants"""
Nf_short = 10**3
Nf_long = 10**5
Nf = np.array([Nf_short, Nf_long, Nf_short, Nf_long])

sigm_pos = sigma_f_prime / 4
sigm_neg = sigma_f_prime / -4
sigma_m = np.array([sigm_pos, sigm_neg, sigm_pos, sigm_neg])

"""Solution Calculations"""
alpha = (((sigma_f_prime - sigma_m) / E) * (2*Nf)**b) + epsilon_f_prime*(2*Nf)**c
beta = (((sigma_f_prime - sigma_m) / E) * ((2*Nf)**b)) + epsilon_f_prime * ((sigma_f_prime - sigma_m)/sigma_f_prime) * (2*Nf)**c

ans = PrettyTable()

#ans.field_names =