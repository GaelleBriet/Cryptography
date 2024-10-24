#### 1 - Inverse modulaire par tâtonnement pour des petits nombres - ####

# 1.1 inverse de 2 modulo 15 (2 * x ≡ 1 [15])
# 2 * 8 ≡ 1 [15]
print(pow(2, -1, 15))

#  1.2 inverse de 5 modulo 29 (5 * x ≡ 1 [29])
# 5 * 6 ≡ 1 [29]
print(pow(5, -1, 29))

# 1.3 inverse de 3 modulo 8 (3 * x ≡ 1 [8])
# 3
print(pow(3, -1, 8))

# 1.4 inverse de 3 modulo 9 (3 * x ≡ 1 [9])
# impossible
# PGCD 9 = 3*3 donc PGCD(3,9) = 3 donc PGCD(3,9) != 1 donc 3 et 9 ne sont pas premiers entre eux
# print(pow(3, -1, 9))

#### 2 - Inverse modulaire par l'algorithme d'Euclide étendu - ####

# 2.1 Programmer une fonction python implémentant l'algorithme d'Euclide étendu

def euclide_etendu(a, b):
    r0, u0, v0, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = r0 // r1 # quotient entier
        r0, u0, v0, r1, u1, v1 = r1, u1, v1, r0 - q * r1, u0 - q * u1, v0 - q * v1
    return u0, v0, r0

# inverse de 79 modulo 23
print(pow(79, -1, 23))