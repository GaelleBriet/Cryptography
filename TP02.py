## 1 - Propriétés de sécurité des fonctions de hachage
import hashlib
import itertools

from cryptography.hazmat.primitives.hashes import SHA3_256


#somme des codes ascii des caractères d'un message
# h = 104, e= 101, l = 108, l = 108, o = 111
# total = 132
def asciihash(message):
    return sum(ord(char) for char in message)
print(asciihash('F<'))

# for a in range(65, 91):  # A à Z
#     for b in range(65, 91):
#         for c in range(65, 91):
#             word = chr(a) + chr(b) + chr(c)
#             if asciihash(word) == 195:
#                 print(f"Le mot trouvé est : {word}")
#                 exit()
# print("Aucun mot trouvé")

# 1-1 - "AAA" vaut 195
# 1-2 - autre message avec la même empreinte que "AA" = "F<"
# 1-3

## ------------------------------- ##

## 2 - SHA-2, SHA-3
from Crypto.Hash import SHA224

def calculate_sha224(message):
    h = SHA224.new()
    h.update(message.encode('utf-8'))
    response = h.hexdigest()
    print(response)
    if response == '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b':
        print('SHA-224 is correct')
    else:
        print('SHA-224 is incorrect')
calculate_sha224('hello world')
# dans le terminal : echo -n 'hello world' | sha224sum | awk '{print $1}'
# 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b

from Crypto.Hash import SHA3_224
from Crypto.Hash import SHA3_256

def calculate_sha3_224(message):
    h = SHA3_224.new()
    h.update(message.encode('utf-8'))
    response = h.hexdigest()
    print(response)
    if response == 'dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5':
        print('SHA3-224 is correct')
    else:
        print('SHA3-224 is incorrect')

calculate_sha3_224('hello world')



## 3 - Brute Force
# hash = d4b19a9d2c50e189321d5ebae2c3f512e002fed309a79e5c78fae14722a178e4
# password = 4 characters
import hashlib
import itertools

#1 - Déterminer les caractères qui peuvent être utilisés dans le mot de passe
#2 - Générer toutes les combinaisons possibles de mots de passe
#3 - Pour chaque combinaison, la convertir en chaines de caractères
# la hacher et comparer le résultat avec le hash cible
# trouver le hash : 64 caractères hexa * 4 = 256 bits


def brute_force(target_hash):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for combination in itertools.product(letters, repeat=4): # itertools.product génère toutes les combinaisons possibles # repeat=4 spécifie que nous cherchons des mots de 4 lettres
        word = ''.join(combination)

        # Utiliser hashlib.sha3_256
        h = hashlib.sha3_256() # Créer un objet de hachage
        h.update(word.encode())  # encode() pour convertir le mot en bytes
        response = h.hexdigest() # hexdigest() pour obtenir le hash en hexadécimal

        if response == target_hash:
            print(f"Le mot trouvé est : {word}")

    print("Aucun mot trouvé")
    return None
# Le hash SHA3-256 pour "GOOD"
target_hash = 'd4b19a9d2c50e189321d5ebae2c3f512e002fed309a79e5c78fae14722a178e4'
print(brute_force(target_hash))

