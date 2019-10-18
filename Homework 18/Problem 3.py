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
Nf = np.array([Nf_short, Nf_short, Nf_long, Nf_long])


sigm_pos = sigma_f_prime / 4
sigm_neg = sigma_f_prime / -4
sigma_m = np.array([sigm_pos, sigm_neg, sigm_pos, sigm_neg])

"""Solution Calculations"""
alpha = (((sigma_f_prime - sigma_m) / E) * (2*Nf)**b) + epsilon_f_prime*(2*Nf)**c
beta = (((sigma_f_prime - sigma_m) / E) * ((2*Nf)**b)) + epsilon_f_prime * ((sigma_f_prime - sigma_m)/sigma_f_prime) * (2*Nf)**c

ans = PrettyTable()

ans.field_names = ["Nf", "Sigma_m","Eq 5.22", "Eq 5.23", "Previous Value"]
ans.add_row(["10^3", "Pos", round(alpha.item(0), 5), round(beta.item(0), 5), 0.00842])
ans.add_row(["10^3", "Neg", round(alpha.item(1), 5), round(beta.item(1), 5), 0.00842])
ans.add_row(["10^5", "Pos", round(alpha.item(2), 5), round(beta.item(2), 5), 0.00195])
ans.add_row(["10^5", "Neg", round(alpha.item(3), 5), round(beta.item(3), 5), 0.00195])

print("SOLUTION")
print(ans)

print("Troubleshooting outputs")
print("NF", Nf)
print("Sigma_m", sigma_m)

print("Comments")
print("")
print("It appeaars that equation 5.22 and 5.23 give answers in roughly "
      "the same order of magnitude as the equations used in problem 5.18.")
print("A notable exception is Eq. 5.23 with a negative mean stress and 10^3 cycles. It is unknown if this a "
      "computing error.")