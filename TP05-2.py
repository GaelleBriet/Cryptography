import math

print(f"------ EXERCICE 1 ------")
# 1. Chiffrement / déchiffrement RSA
# 1.1. Déterminer la clé publique et la clé privée pour p = 53 et q = 61
## On prendra e = 17 et on s'assurera que ce choix est possible

e = 17

# on calcule N = pq et phi(N) = (p-1)(q-1)
N = 53 * 61
phi_N = (53-1) * (61-1)
print(f"N = {N}, phi(N) = {phi_N}")

# on vérifie que e et phi(N) sont bien premiers entre eux (PGCD par algorithme d'Euclide)
# 3120 / 17 = 183.52941176470588
# 183 * 17 = 3111
# 3120 - 3111 = 9
# donc 3120 = 183 * 17 + 9
# 17 / 9 = 1
# 9 / 8 = 1
# 8 / 1 = 8
# 1 / 0 = 1
# PGCD = 1
# on peut donc choisir e = 17

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if pgcd(e, phi_N) == 1:
    print(f"{e} et {phi_N} sont premiers entre eux.")
# on calcule la clé privée d = e^-1 mod phi(N)  - (inverse de e modulo phi(N))
d = pow(e, -1, phi_N)
# la clé publique est (N, e) et la clé secrète est l'entier d
print(f"Clé secrète : d = {d}")
print(f"Clé publique : (N, e) = ({N}, {e})")

# 1.2 chiffrer le message M = 66
# c = M^e mod N
M = 66
c = pow(M, e, N)
print(f"Message chiffré : {c}")

# 1.3 Utiliser la clé privée pour déchiffrer le message obtenu et vérifier qye l'on retrouve M.
# M = c^d mod N
M_decrypt = pow(c, d, N)
print(f"Message déchiffré : {M_decrypt}")


## -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 2 ------")
# 2. Décryptage RSA
# 2.1 On considère maintenant la clé publique (N,e) = (299,5)
# Calculer la clé privée pour déchiffrer le message C = 123

#Calculer la clé privée : Factoriser N = 299 avec Dcode 299 = 13 * 23
p = 13
q = 23
N = p * q
# Calculer phi(N) = (p-1)(q-1)
phi_N = (p-1) * (q-1)
# Trouver d = e^-1 mod phi(N)
e = 5
d = pow(e, -1, phi_N)
print(f" Clé secrète : d = {d}")

# Déchiffrer => C^d mod N
C = 123
M = pow(C, d, N)
print(f"Message déchiffré : {M}")

# 2.2 Peut-on obtenir le message codé 435 avec cette clé publique ?
print(f"Message codé 435 n'est pas possible car supérieur à N")


## -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 3 ------")
# 3. Factorisation par divisions successives
# Écrire une fonction qui renvoie le plus petit facteur de n
# essayer tous les entiers à partir de 2 jusqu'à racine de n
def lowest_divisor(n):
    # vérifier si n est divisible par 2
    if n % 2 == 0 :
        return 2
    # si pas divisible par 2, on teste les nombres impaires jusqu'à racine de n
    # on commence à 3 , jusqu'à racine de n, de 2 en 2
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return i
    # si aucun facteur n'a été trouvé, n est premier
    return n

# Factoriser l'entier N = 1401648848139749549713911598083881229189946002109872707904319
# et déchiffrer le message 727730560734235226753826924909974886886905610591708056596328
# avec e = 65537
N = 1401648848139749549713911598083881229189946002109872707904319
M = 727730560734235226753826924909974886886905610591708056596328
e = 65537

# Factoriser N
p = lowest_divisor(N)
print(f"plus petit facteur n de N = {p}")

# Trouver l'autre facteur
q = N // p
print(f"autre facteur m de N = {q}")

# Calculer phi(N) = (p-1)(q-1)
phi_N = (p-1) * (q-1)
# Clé privée d = e^-1 mod phi(N)
d = pow(e, -1, phi_N)
# Déchiffrer le message C^d mod N
m = pow(M, d, N)
print(f"Message déchiffré : {m}")

# convertir le message déchiffré en bytes
message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
print(f"Message déchiffré en bytes : {message}")



## -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 4 ------")
# 4. Factorisation par la méthode de Fermat

def fermatfact(n):
    # for a in range(int(n**0.5),int((n+9)/6) +1):
    a = math.isqrt(n)  # donne la partie entière inférieure de la racine carrée
    limite = (n + 9) // 6
    while a <= limite:
        # b = √(a² - n)
        b_carre = a*a - n
        if b_carre < 0:
            continue

        b = math.isqrt(b_carre)
        if b*b == b_carre :
            return a - b

    return "PREMIER"

# Factoriser N
N = 722004061052679563836535567898293033224272840624350671385483

print("Début factorisation avec fermatfact()...")
facteur = fermatfact(N)
if facteur != "PREMIER":
    print(f"Facteur trouvé : {facteur}")
    autre_facteur = N // facteur
    print(f"L'autre facteur : {autre_facteur}")
    print(f"Vérification : {facteur * autre_facteur == N}")