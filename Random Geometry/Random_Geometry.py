import math  # Importing
import random  # Libraries

# Asking for Parameters
p = int(input("Enter the number of different species  "))
K = {}
n = 0
print("Input details fo all the different species:")
for i in range(p):
    K[i] = {}
    s = input("\t Enter the symbol of species  ")
    m = int(input("\t Enter the number of atom of that species  "))
    K[i][0] = s
    K[i][1] = m
    n = n + m
print("\n")
g1 = int(input("Enter the number of One Dimensional Geometries  "))
g2 = int(input("Enter the number of Two Dimensional Geometries  "))
g3 = int(input("Enter the number of Three Dimensional Geometries  "))
tol = float(input("Enter the minimum spacing between atoms in (0.05-0.2)Angstrom"))

# One Dimensional Geometries 
# Range of region varies from 0 to 2*n Angstrom
G1 = {}
flag = 0
for i in range(g1):
    G1[i] = {}
    for j in range(n):
        condition = True
        flag = 0
        while condition:
            G1[i][j] = (random.uniform(0.000, 2*n), 0, 0)
            condition = False
            if j > 0:
                for k in range(j):
                    dist = math.sqrt((G1[i][j][0] - G1[i][k][0]) ** 2 + (G1[i][j][1] - G1[i][k][1]) ** 2 + (
                            G1[i][j][2] - G1[i][k][2]) ** 2)
                    if dist < tol:
                        condition = True
# Two Dimensional Geometries
# Range of region varies from 0 to 2*n Angstrom
G2 = {}
flag = 0
for i in range(g2):
    G2[i] = {}
    for j in range(n):
        condition = True
        flag = 0
        while condition:
            G2[i][j] = (random.uniform(0.000,2* n), random.uniform(0.000, 2*n), 0)
            condition = False
            if j > 0:
                for k in range(j):
                    dist = math.sqrt((G2[i][j][0] - G2[i][k][0]) ** 2 + (G2[i][j][1] - G2[i][k][1]) ** 2 + (
                            G2[i][j][2] - G2[i][k][2]) ** 2)
                    if dist < tol:
                        condition = True
# Three Dimensional Geometries
# Range of region varies from 0 to 2*n Angstrom
G3 = {}
flag = 0
for i in range(g3):
    G3[i] = {}
    for j in range(n):
        condition = True
        flag = 0
        while condition:
            G3[i][j] = (random.uniform(0.000,2* n), random.uniform(0.000,2* n), random.uniform(0.000, 2*n))
            condition = False
            if j > 0:
                for k in range(j):
                    dist = math.sqrt((G3[i][j][0] - G3[i][k][0]) ** 2 + (G3[i][j][1] - G3[i][k][1]) ** 2 + (
                            G3[i][j][2] - G3[i][k][2]) ** 2)
                    if dist < tol:
                        condition = True
# Printing the results
print("\n")
print("One Dimensional Geometries are: ")
q = 0
l = 0
for i in range(g1):
    print("\n")
    print("Geometry", i + 1, " : ")
    print("\n")
    q = 0
    l = 0
    for j in range(n):
        if l < K[q][1]:
            print("\t atom  ", G1[i][j][0], "   ", G1[i][j][1], "   ", G1[i][j][2], "  ", K[q][0])
            l = l + 1
        else:
            q = q + 1
            l = 0
            print("\t atom  ", G1[i][j][0], "   ", G1[i][j][1], "   ", G1[i][j][2], "  ", K[q][0])
            l = l + 1
print("\n")
q = 0
l = 0
print("Two Dimensional Geometries are: ")
for i in range(g1):
    print("\n")
    print("Geometry", i + 1, " : ")
    print("\n")
    q = 0
    l = 0
    for j in range(n):
        if l < K[q][1]:
            print("\t atom  ", G2[i][j][0], "   ", G2[i][j][1], "   ", G2[i][j][2], "  ", K[q][0])
            l = l + 1
        else:
            q = q + 1
            l = 0
            print("\t atom  ", G2[i][j][0], "   ", G2[i][j][1], "   ", G2[i][j][2], "  ", K[q][0])
            l = l + 1
print("\n")
q = 0
l = 0
print("Three Dimensional Geometries are: ")
for i in range(g1):
    print("\n")
    print("Geometry", i + 1, " : ")
    print("\n")
    q = 0
    l = 0
    for j in range(n):
        if l < K[q][1]:
            print("\t atom  ", G3[i][j][0], "   ", G3[i][j][1], "   ", G3[i][j][2], "  ", K[q][0])
            l = l + 1
        else:
            q = q + 1
            l = 0
            print("\t atom  ", G3[i][j][0], "   ", G3[i][j][1], "   ", G3[i][j][2], "  ", K[q][0])
            l = l + 1
