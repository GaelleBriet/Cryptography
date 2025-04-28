## -- -- -- -- -- -- -- -- -- ##
from math import gcd

print(f"------ EXERCICE 1 ------")
# Factorisation par la méthode rho de Pollard
# Écrire une fonction rho_pollard(n) qui applique la méthode du rho de Pollard pour trouver une
# factorisation de l'entier n

def rho_pollard(n):
    # Initialisation
    x = 2
    y = x
    div = 1
    # Fonction de calcul de f(x)
    while div == 1:
        # Fonction F(x) = x^2 + 1 (mod n)
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        # Calcul du PGCD
        # si x = 15 y = 3 n = 20
        # |x-y| = |15-3| = 12
        # PGCD(12, 20) = 4
        diff = abs(x - y)    # Valeur absolue de x-y
        div = gcd(diff, n)   # PGCD(|x-y|, n)
    if div == n :
        return "ECHEC"
    else:
        return div

N = 735823367082045355636236031841
c = 513711620132246923659868689721
e = 65537

print(f"Factorisation de N ...")
p = rho_pollard(N)
q = N // p
print(f"p = {p}")
print(f"q = {q}")

# calcul de phi(N)
phi_N = (p - 1) * (q - 1)
print(f"phi(N) = {phi_N}")

# calcul de d
d = pow(e, -1, phi_N)
print(f"d = {d}")

# déchiffrer le message m
# m = c^d mod N
m = pow(c, d, N)
print(f"m = {m}")


# convertir l'entier m en chaine de caractères
message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
print(f"message décodé= {message}")

print(f"------ EXERCICE 2 ------")
print(f"...")
print(f"....")
print(f".....")
print(f"..... BOOM !")