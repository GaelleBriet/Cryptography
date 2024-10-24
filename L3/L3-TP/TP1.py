## -- 1 -- Chiffrement par décalage (shift cipher) ou chiffrement de César ##

## -- 1.1 Chiffrement -- Écrire une fonction encryptcesar(plaintext, key=3) qui chiffre le message plaintext avec un
## décalage key qui vaudra 3 par défaut.##

def encryptcesar(plaintext, key = 3):
    plaintext = plaintext.upper()
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lettersToEncrypt = []

    for letter in plaintext:
        if letter in letters:
            # find the index of the letter in the list
            i = letters.index(letter)
            # add the index to the key
            j = (i + key) % 26
            # add the letter to the list
            lettersToEncrypt.append(letters[j])
        elif letter == ' ':
            lettersToEncrypt.append(' ')
    crypted_message = ''.join(lettersToEncrypt)
    print(crypted_message)

encryptcesar('AvE CEsAR', 7)

## -------------------------------------------------------------------------------------------------------------  ##

## -- 1.2 Déchiffrement -- Utiliser la fonction écrite pour déchiffrer le message suivant
# obtenu avec une clé de 17: FBKFLKMRSZVE ##

def decrypt_cesar(crypted_message, key = 3):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lettersToDecrypt = []
    for letter in crypted_message:
        if letter in letters:
            i = letters.index(letter)
            j = (i - key) % 26
            lettersToDecrypt.append(letters[j])
        elif letter == ' ':
            lettersToDecrypt.append(' ')
    decrypted_message = ''.join(lettersToDecrypt)
    print(decrypted_message)

decrypt_cesar('FBKFLKMRSZVE', 17)

## -------------------------------------------------------------------------------------------------------------  ##

## -- 1.3 Attaque par force brute -- Écrire une fonction bruteforcecesar(ciphertext) qui décrypte
# le message ciphertext sans connaître la clé, en utilisant une attaque par force brute ##

def bruteforcecesar(ciphertext):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lettersToDecrypt = []
    most_frequent_letter = max(set(ciphertext), key = ciphertext.count)
    j = 0
    key = 0
    # on base l'algo sur la recherche de la lettre la plus utilisée en français : le E
    if most_frequent_letter in letters:
        i = letters.index(most_frequent_letter)
        # on calcul la clef à partir de l'index de E comparé à l'index de la lettre la plus représentée
        if i > 4 :
            key = (i - 4) % 26
    # on reprends l'algo de base
    for letter in ciphertext:
        i = letters.index(letter)
        j = (i - key) % 26
        lettersToDecrypt.append(letters[j])
    decrypted_message = ''.join(lettersToDecrypt)

    print(f"La clef utilisée est {key} pour déchiffrer le message : {decrypted_message}")
bruteforcecesar('CVPSHSLZBWLYTLZZHNL')

## -------------------------------------------------------------------------------------------------------------  ##

## -- 1.4 Chiffre ROT13-- Utiliser la fonction encryptcesar pour déchiffrer le message suivant chiffré en ROT13
# PUVSSER ZBV HAR QRHKVRZR SBVF RG BOFREIR YR ERFHYGNG ##

encryptcesar('PUVSSER ZBV HAR QRHKVRZR SBVF RG BOFREIR YR ERFHYGNG', 13)
encryptcesar('CHIFFRE MOI UNE DEUXIEME FOIS ET OBSERVE LE RESULTAT', 13)

## BONUS A FAIRE ##


## -------------------------------------------------------------------------------------------------------------  ##

## -- 2 -- Chiffre Atbash ##
## -- Écrire une fonction encrypt_atbash(plaintext) qui calcule le chiffrement par le chiffre Atbash. -- ##
## -- Déchiffrer le message suivant: GILK UZXROV XV XSRUUIV ZGYZHS -- ##

def encrypt_atbash(plaintext):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    plaintext = plaintext.upper()
    crypted_letters = []

    for letter in plaintext:
        if letter in letters:
            init_pos = letters.index(letter)
            new_pos = 25 - init_pos
            crypted_letters.append(letters[new_pos])
        elif letter == ' ':
            crypted_letters.append(' ')

    crypted_message = ''.join(crypted_letters)
    print(crypted_message)

encrypt_atbash('GILK UZXROV XV XSRUUIV ZGYZHS')

## BONUS A FAIRE ##

## -------------------------------------------------------------------------------------------------------------  ##

## -- 3 -- Chiffre Pigpen ou chiffre des francs-maçons ##
## -- Déchiffrer le message  -- ##

def create_pigpen_cipher():
    # Création du dictionnaire de décodage
    cipher = {
        '⊓': 'A', '⊔': 'B', '⊏': 'C', '⊐': 'D', '⊢': 'E',
        '∟': 'F', '⊤': 'G', '⊥': 'H', '⊣': 'I', '|_': 'J',
        '|¯': 'K', '|‾': 'L', '|–': 'M', '⌊': 'N', '⌋': 'O',
        '⌈': 'P', '⌉': 'Q', '∠': 'R', '∟': 'S', '⊾': 'T',
        '⊿': 'U', '∧': 'V', '∨': 'W', '⋏': 'X', '⋎': 'Y', '⊼': 'Z'
    }
    return cipher

def decrypt_pigpen(message):
##



