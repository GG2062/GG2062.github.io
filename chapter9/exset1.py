
#exSet1.py

A = {1,2,3,4,5,7}
B = {0,2,3,6,8}
C = {4,6,8,10}
U = {0,1,2,3,4,5,6,7,8,9,10}

#E = A.union(B)
E = A | B
print(f'A U B = {E}')

#N = A.intersection(B)
N = A & B
print(f'A and B = {N}')

#AminusB  = A.difference(B)
AminusB = A-B
print(f'A-B = {AminusB}')

BminusA = B-A
print(f'B-A = {BminusA}')
print()

#F = A.symmetric_difference(B)
F = A ^ B
print(f'Symmetric difference = {F}')

F = (A-B) | (B-A)
print(f'F = {F}')

CC = U - C
print(f'C = {CC}')

x = A | (B & C)
print(f'A U (B & C) = {x}')
print()

Y = A - ((U-B) & (U-C))
print(f'Y = {Y}')


