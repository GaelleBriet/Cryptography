from random import randint

from Crypto.Util.number import long_to_bytes

print(f"------ TP 9 ------")
print(f"------ Cryptosystème ElGamal ------")
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 1 : Chiffrement/Déchiffrement------")
print(f"------ 1.1 ------")

# 1. Écrire une fonction encrypt_elgamal(m, p, g, y) qui renvoie le tuple (c1, c2) correspondant
# au chiffrement du message m selon le chiffrement ElGamal de paramètres p, g, y
# On choisit p = 13, g = 2, et x = 9.
# Chiffrer le message m = 11 plusieurs fois. Que remarque-t-on?
g = 2
p = 13
x = 9
y = pow(g, x, p)
def encrypt_elgamal(m, p, g, y):
    k = randint(1, p-1)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    # c2 = m * pow(y, k, p)
    return (c1, c2)

print(f"Chiffrement de 11 avec p = 13, g = 2, x = 9: {encrypt_elgamal(11, 13, 2, y)}")
print(f"On remarque que le chiffrement est différent à chaque fois")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
print(f"------ 1.2 ------")

# 2. Écrire la fonction de déchiffrement decrypt_elgamal(c, p, x) qui déchiffre le tuple chiffré c.
# Déchiffrer différentes valeurs trouvées à la question précédente et vérifier que l'on retrouve toujours
# le message m = 11.
# Déchiffrer le message (478923389, 552338072) avec p = 702450227, x = 4242 qui correspond à des
# octets formant un tout petit mot

def decrypt_elgamal(c, p, x):
    c1, c2 = c
    m = (c2 * pow(c1, -x, p)) % p
    return m

print(f"Déchiffrement de 2, 3) avec p = 13, x = 9: {decrypt_elgamal((2, 3), 13, 9)}")
print(f"Déchiffrement de 3, 11) avec p = 13, x = 9: {decrypt_elgamal((3, 11), 13, 9)}")
print(f"Déchiffrement de (478923389, 552338072) avec p = 702450227, x = 4242: {decrypt_elgamal((478923389, 552338072), 702450227, 4242)}")
code_octets = decrypt_elgamal((478923389, 552338072), 702450227, 4242)
print("Message déchiffré : ", long_to_bytes(code_octets))

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 2 : Attaque sur aléa fixe ------")

# Les chirés interceptés sont:
# (318923637155957880733060818348671592175670177, 623526122783521939335330180409853741575115586)
# (318923637155957880733060818348671592175670177, 550722152549623511080871652100870764848994915)
# On voit que la première partie des chirés est la même et on suppose qu'Alice utilise tout le temps la
# même clé k pour chirer son message au lieu de tirer cette valeur aléatoirement.
# D'autre part, on pense que le deuxième message est 'ok'.
# La clé publique de Bob est:
# p = 716284341302167000055184842023375412267242919
# g = 2
# y = 605469578809314635851173503246145223480932021
# Retrouver le premier message d'Alice.
p = 716284341302167000055184842023375412267242919
g = 2
y = 605469578809314635851173503246145223480932021

c1 = 318923637155957880733060818348671592175670177
c2 = 623526122783521939335330180409853741575115586
c2_1 = 550722152549623511080871652100870764848994915
# message 1 = (c1, c2)
# message 2 = (c1, c2_1) # ou (c1_1, c2_1)
# message 2 = 'ok'
m2 = int.from_bytes(b"ok", "big")
print(f"m2 = {m2}") # 28523

m1 = (c2 * pow(c2_1, p - 2, p) * m2) % p
print(f"m1 = {m1}") # 2321553641674501673619680857830248

msg = bytes.fromhex(hex(m1)[2:]).decode('utf-8')
print(f"Message déchiffré : {msg}")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 3  : Hackropole------")

print(f"flag hackropole El Gamal fait 1/2 = FCSC-9494cb0e1aad8257099a1d1c146b740f01cd9573b26de3370bdd9d09aadcff54")

