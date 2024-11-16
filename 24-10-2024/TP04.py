#### 1 - Inverse modulaire par tâtonnement pour des petits nombres - ####
from pydoc import plaintext, plain

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

# 2.2 utiliser la fonction pour trouver l'inverse de 79 modulo 23
print(f"inverse 79 modulo 23 avec la fonction écrite", euclide_etendu(79, 23))

# 2.3 vérifier que 79 × 79−1 ≡ 1 (mod 23)
# utiliser l'algo euclide etendu pour trouver l'inverse de 79 modulo 23 appelé u
u, v, r = euclide_etendu(79, 23)
inverse = u
# calculer 79 * u modulo 23
resultat = (79 * inverse) % 23
print(f"79 * {inverse} ≡ {resultat} (mod 23)")

# 2.4 calculer l'inverse de 79 modulo 23 en utilisant pow
print(f"inverse 79 modulo 23 avec pow",pow(79, -1, 23))


#### 3 - Inversion modulaire pour inverser la fonction RSA - ####

ciphertext = b'\xb1\xa2\x0f\x18\xb0\xd7\x81-H\x19\x1bW\xbcf$\xa8\x98\x8b\xdf\xbe\xf1\x0f\xcf\x97\xe1>\x99?\x19G\x8aie\x980^\x99F\x1aD\xed\x12{\x19\xe7\t\xba\x86'
# chiffré avec un AES en mode GCM avec le nonce :
nonce = b'\x1b\xda3\xac\x87\xcdM\xd7\x18\x12\x8djbT\xee\x02'
# clé chiffrée par RSA :
c = 64058176184997834950693853025106406054
# clé publique donnée par :
N = 236162332383177856298590687609142183389
e = 65537

# 3.1 Factoriser N pour calculer φ(N ) = (p − 1)(q − 1)
# on peut utiliser un outil tel que Dcode
# https://www.dcode.fr/decomposition-nombres-premiers
# https://www.wolframalpha.com/ factorize 236162332383177856298590687609142183389
p = 12864203442245594737
q = 18358099935486794797
phi_N = (p-1) * (q-1)
# N = p * q
print(f"Factoriser N pour calculer φ(N ) = (p − 1)(q − 1)= ", phi_N)

# 3.2 Vérifier que e et φ(N ) sont bien premiers entre eux et retrouver la clé secrète d
# inverse de e modulo φ(N )
# e * x ≡ 1 [phi_N]
d = pow(e, -1, phi_N)
print(f"inverse de e modulo φ(N )", d)

# Vérification que d est correct
verification = (e * d) % phi_N
print(f"Vérification : e * d mod φ(N) = {verification}")

# 3.3 avec la clé secrète d, déchiffrer la clé du chiffrement AES c
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad

def rsa_decrypt(c, d, N):
    return pow(c, d, N)
decrypted_key = rsa_decrypt(c, d, N)
print(f"Clé AES décryptée :", decrypted_key)

# 3.4 Déchiffrer le message avec la clé secrète
# convertir la clé déchiffrée en bytes (16  bytes pour AES)
key_bytes = decrypted_key.to_bytes(16, byteorder='big')
def aes_gcm_decrypt(ciphertext, key, nonce):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

decrypted_message = aes_gcm_decrypt(ciphertext, key_bytes , nonce)
print(f"Message déchiffré :", decrypted_message.decode('utf-8'))


#### 4 - Bonus: RSA sur hackropole - ####
# 4.1 - Résoudre le challenge SMIC(2)
# La sécurité du cryptosystème RSA repose sur un problème calculatoire bien connu.
# On vous demande de déchiffrer le “message” chiffré c ci-dessous pour retrouver le “message” en clair m associé à partir de la clé publique (n, e).
e = 65537
n = 632459103267572196107100983820469021721602147490918660274601
c = 63775417045544543594281416329767355155835033510382720735973
# c = m^e mod n
# m = c^d mod n
# d = e^-1 mod phi(n)
# phi(n) = (p-1)(q-1)
# n = p*q
# factoriser n pour trouver p et q
# Factoriser N pour calculer φ(N ) = (p − 1)(q − 1)
# 650655447295098801102272374367 × 972033825117160941379425504503


# 4.2 - Résoudre le challenge "Rien à signaler"