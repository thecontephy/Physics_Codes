import math  # Importing
import numpy as np  # Necessary
import matplotlib.pyplot as plt  # Libraries

# Taking R2/y constant.
y = float(input("What is the value of R2?"))
r1 = float(input("What is the start value of R1?"))
r2 = float(input("What is the end value of R1?"))
c = float(input("What is the step value of R1?"))

# Range for R1/x values.
X = np.arange(r1, r2, c)

A = np.arange(r1, r2, c / 2)  # psi(1,2) values for different R1 and R2
B = np.arange(r1, r2, c / 2)  # psi(2,1) values for different R1 and R2
p = len(A) - 1

for ind, x in enumerate(X):
    k = p - ind - 1
    A[k] = float((8 / 3.14) * (math.exp(-4 * x)) * (1 / 3.14) * (1 - 2 * y + y * y) * (math.exp(-2 * y)))
    B[k] = float((8 / 3.14) * (math.exp(-4 * y)) * (1 / 3.14) * (1 - 2 * x + x * x) * (math.exp(-2 * x)))
for ind, x in enumerate(X):
    k = p + ind
    A[k] = float((8 / 3.14) * (math.exp(-4 * x)) * (1 / 3.14) * (1 - 2 * y + y * y) * (math.exp(-2 * y)))
    B[k] = float((8 / 3.14) * (math.exp(-4 * y)) * (1 / 3.14) * (1 - 2 * x + x * x) * (math.exp(-2 * x)))

########################################################################################################
S = np.arange(r1, r2, c / 2)  # Symmetric Solution
AS = np.arange(r1, r2, c / 2)  # Anti-Symmetric Solution

########################################################################################################
for ind, x in enumerate(A):
    S[ind] = ((A[ind] + B[ind]) ** 2) / 2
    AS[ind] = ((A[ind] - B[ind]) ** 2) / 2
J = (r1, r2, 2 * c)
for ind, x in enumerate(X):
    k = p + ind - 1
    J[k] = (-(X[ind] - y))
for ind, x in enumerate(X):
    J[k] = (X[ind] - y)

####################################.........Graph Plotting........#########################################
fig, ax1 = plt.subplots()
ax1.plot(J, S, 'b-')
ax1.set_xlabel('|R1-R2|')
ax1.set_ylabel('Symmetric Probability Distribution', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(J, AS, 'r-')
ax2.set_ylabel('Anti-Symmetric Probability Distribution', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()

