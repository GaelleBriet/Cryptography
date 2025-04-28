print(f"------ TP 7 ------")
print(f"------ Attaques sur chiffrement RSA - Utilisation de RSA-OAEP ------")
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 1 : Attaque sur petits textes clairs ------")
# Le message chiffré contenu dans le fichier exo1.cipher a été obtenu en utilisant
# la clé publique contenue dans le fichier exo1key.pem

print(f"------ 1.1 ")
# Utiliser la fonction RSA.import_key de la librairie Crypto.PublicKey pour lire la clé contenue dans le fichier exo1key.pem et observer les valeurs de n et e.
import Crypto.PublicKey.RSA as RSA
key = RSA.import_key(open("TP7_data/exo1key.pem").read())
print(f"clé exo1key.pem : n = {key.n}")
print(f"clé exo1key.pem : e = {key.e}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 1.2 ")
# Ouvrir le fichier exo1.cipher en lecture binaire (option rb de la fonction open) et retrouver le nombre associé en utilisant la fonction int.from_bytes.
with open("TP7_data/exo1.cipher", "rb") as f:
    cipher = int.from_bytes(f.read(), "big")
print(f"exo1.cipher : {cipher}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 1.3 ")
# On a vu que e est de petite taille. Si le message clair m est de petite taille il se peut que me < N . Utiliser la fonction integer_nthroot de la librarie sympy pour calculer la racine e-ième de m
# pip3 install sympy
from sympy import integer_nthroot
m, _ = integer_nthroot(cipher, key.e)
print(f"exo1.cipher : m = {m}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 1.4 ")
# Retrouver le message m en utilisant la fonction long_to_bytes de la librairie Crypto.Util.number
from Crypto.Util.number import long_to_bytes
print(f"exo1.cipher : m = {long_to_bytes(m).decode()}")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 2 : Attaque par module commun ------")
# Les fichiers alicekey.pem et bobkey.pem correspondent aux clés publiques de Alice et Bob.

print(f"------ 2.1 ")
# Importer les deux clés. Observer leurs modules et leurs exposants. Que remarquez-vous?
alice_key = RSA.import_key(open("TP7_data/alicekey.pem").read())
bob_key = RSA.import_key(open("TP7_data/bobkey.pem").read())
print(f"alicekey.pem : n = {alice_key.n}")
print(f"alicekey.pem : e = {alice_key.e}")
print(f"bobkey.pem : n = {bob_key.n}")
print(f"bobkey.pem : e = {bob_key.e}")
print(f"Les modules sont les mêmes, les exposants sont différents.")
## -- -- -- -- -- -- -- -- ##

print(f"------ 2.2 ")
# Les fichiers alice.cipher et bob.cipher correspondent au même message chiffré par Alice et par Bob.
# Construire les nombres ciphera et cipherb correspondant.
with open("TP7_data/alice.cipher", "rb") as f:
    ciphera = int.from_bytes(f.read(), "big")
with open("TP7_data/bob.cipher", "rb") as f:
    cipherb = int.from_bytes(f.read(), "big")
print(f"alice.cipher : {ciphera}")
print(f"bob.cipher : {cipherb}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 2.3 ")
# Les exposants ea et eb des clés publiques de Alice et Bob étant premiers entre eux, l'algorithme
# d'euclide étendu permet de calculer les coefficients de Bézout u et v tels que u × ea + v × eb = 1.

# Le script suivant correspond à l'algorithme d'Euclide étendu:
# def extended_euclidian(a, b):
# r, u, v, r1, u1, v1 = a, 1, 0, b, 0, 1
# while r1!=0:
# q = r // r1
# r, u, v, r1, u1, v1 = r1, u1, v1, r-q*r1, u-q*u1, v-q*v1
# return (u, v, r)

# Calculer u et v.
# En déduire m en calculant ((cipherau (mod na)) × (cipherbv (mod na))) (mod na)

def extended_euclidian(a, b):
    r, u, v, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1!=0:
        q = r // r1
        r, u, v, r1, u1, v1 = r1, u1, v1, r-q*r1, u-q*u1, v-q*v1
    return (u, v, r)

u, v, _ = extended_euclidian(alice_key.e, bob_key.e)
m = (pow(ciphera, u, alice_key.n) * pow(cipherb, v, alice_key.n)) % alice_key.n
print(f"m = {m}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 2.4 ")
# Habituellement, le chiffrement RSA est utilisé pour chiffrer des clés.
# Dans cet exercice, un message a été chiffré. Retrouver le message m.
print(f"m = {long_to_bytes(m).decode()}")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 3 : Utilisation de RSA-OAEP------")

print(f"------ 3.1 ")
# Construire une paire de clés RSA avec le module RSA de Crypto.PublicKey.
key = RSA.generate(2048)
print(f"n = {key.n}")
print(f"e = {key.e}")
print(f"d = {key.d}")
## -- -- -- -- -- -- -- -- ##

print(f"------ 3.2 ")
# Chiffrez un message de votre choix avec le protocole RSA-OAEP. Observez le chiffré obtenu.
from Crypto.Cipher import PKCS1_OAEP
message = "Bonne année 2025!"
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message.encode())
print(f"message = {message}")
print(f"ciphertext = {ciphertext}")
print(f"len(ciphertext) = {len(ciphertext)}")
print(f"len(message) = {len(message)}")
print(f"le chiffré est plus long que le message.")
## -- -- -- -- -- -- -- -- ##

print(f"------ 3.3 ")
# Chiffrez à nouveau votre message et observez le chiffré obtenu. Que remarquez-vous?
ciphertext2 = cipher.encrypt(message.encode())
print(f"ciphertext2 = {ciphertext2}")
print(f"len(ciphertext2) = {len(ciphertext2)}")
print(f"le chiffré est différent.")
## -- -- -- -- -- -- -- -- ##

print(f"------ 3.4 ")
# Déchiffrez vos deux chiffrés et vérifiez que vous retrouvez votre message.
message1 = cipher.decrypt(ciphertext)
print(f"message1 = {message1.decode()}")
message2 = cipher.decrypt(ciphertext2)
print(f"message2 = {message2.decode()}")
## -- -- -- -- -- -- -- -- ##

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
print(f"------ EXERCICE 4 : Bonus - Attaque par petit exposant commun - Attaque par Håstad------")
# Alice, Bob et Caroll ont les clés publiques suivantes:
# (Na = 600546705925241516811764674164468940862481993848336751585437, e = 3)
# (Nb = 821052152797996591916092419591478173981510087546741262380757, e = 3)
# (Nc = 885726843897740204564877425284587637172656452057698159034967, e = 3)
# Oscar envoie à chacun d'eux le même message chiffré avec leurs clés.
# Les chiffrés obtenus sont:
# ca = 577089273249993552456065698457946698545999835543854506358245
# cb = 279480358435289773813360585189161043661997736473574268805680
# cc = 631061683309129986079589534259913874858332134592489950754587
# Retrouver ce message

# Remarque:
# on peut utiliser la formule donnée dans le cours ou utiliser la fonction crt (Chinese Remainder Theorem)
# de sympy.ntheory.modular par exemple.

from sympy.ntheory.modular import crt
from sympy import integer_nthroot
from Crypto.Util.number import long_to_bytes

Na = 600546705925241516811764674164468940862481993848336751585437
Nb = 821052152797996591916092419591478173981510087546741262380757
Nc = 885726843897740204564877425284587637172656452057698159034967
e = 3
ca = 577089273249993552456065698457946698545999835543854506358245
cb = 279480358435289773813360585189161043661997736473574268805680
cc = 631061683309129986079589534259913874858332134592489950754587

# on utilise la fonction crt
m, _ = crt([Na, Nb, Nc], [ca, cb, cc])

m_root, exact = integer_nthroot(m, 3)
if not exact:
    m_root += 1
print(f"m = {m}")
message = long_to_bytes(m_root).decode('utf-8', errors='ignore')
print(f"Message: {message}")
## -- -- -- -- -- -- -- -- ##



