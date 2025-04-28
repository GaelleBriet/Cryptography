print(f"------ TP 8 ------")
print(f"------ Problème du Logarithme discret -Échange de clé de Diffie Hellman ------")
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 1 : Échange de cké de Diffie et Hellman ------")

# Alice et Bob veulent partager une clé par le protocole de Diffie et Hellman.
# Ils ont choisi p = 11 et g = 2 comme générateur de (Z/11Z∗)

print(f"------ 1.1 ------")

# Vérifier que 2 est bien un générateur de (Z/11Z∗) c'est-à-dire que les puissances de 2 modulo 11
# donnent les nombres de 1 à 10. On peut utiliser set par exemple
# Vérifier que 2 est bien un générateur de (Z/11Z∗) c'est-à-dire que les puissances de 2 modulo 11
# donnent les nombres de 1 à 10. On peut utiliser set par exemple
p = 11
g = 2
generateur = {pow(g, i, p) for i in range(1, p)}
print(f"Generated set: {generateur}")
print(f"2 est un générateur de (Z/11Z∗): {generateur == set(range(1, p))}")
print(f"2 est bien un générateur de (Z/11Z∗), c'est-à-dire que les puissances de 2 modulo 11 donnent les nombres de 1 à 10")

# Calculer (2^0 \mod 11):
# 2^0 = 1 (tout nombre élevé à la puissance 0 est égal à 1)
# 1 \mod 11 = 1  (=> reste de la division euclidienne de 1 par 11 => 1/11 = 0 reste 1)

# Calculer (2^1 \mod 11):
# 2^1 = 2 (tout nombre élevé à la puissance 1 est égal à lui-même)
# 2 \mod 11 = 2 (=> reste de la division euclidienne de 2 par 11 => 2/11 = 0 reste 2)

# Calculer (2^2 \mod 11):
# 2^2 = 4 ( 2*2 = 4)
# 4 \mod 11 = 4 (=> reste de la division euclidienne de 4 par 11 => 4/11 = 0 reste 4)

print(f"------ 1.2 ------")
# Pourraient-ils choisir 3 comme générateur de (Z/11Z∗)?
p = 11
g = 3
generateur = {pow(g, i, p) for i in range(1, p)}
print(f"Generated set: {generateur}")
print(f"3 est un générateur de (Z/11Z∗): {generateur == set(range(1, p))}")
print(f"3 n'est pas un générateur de (Z/11Z∗), c'est-à-dire que les puissances de 3 modulo 11 ne donnent pas les nombres de 1 à 10. Ici seulement 1, 3, 4, 5, 9")

print(f"------ 1.3 ------")
# Avec p = 11 et g = 2, Alice choisit le nombre secret a = 4 et Bob choisit le nombre secret b = 8.
# Calculer la clé partagée et vérifier que Bob et Alice trouvent bien la même clé.

p = 11
g = 2
a = 4
b = 8

Ka = pow(g, a, p)
Kb = pow(g, b, p)

print(f"Calcul de Ka par Alice: {Ka}")
print(f"Calcul de Kb par Bob: {Kb}")

Kab = pow(g, a*b, p)
Kba = pow(g, b*a, p)

print(f"Clé partagée par Alice: {Kab}, Clé partagée par Bob: {Kba}. Les deux clés sont bien identiques")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 2 : Logarithme discret: brute force ------")

# Alice et Bob veulent partager une nouvelle clé par le protocole de Diffie et Hellman.
# Ils ont choisi p = 13 et g = 6 comme générateur de (Z/13Z∗).
# Oscar a intercepté la valeur Ka = 5.

print(f"------ 2.1 ------")
# Utiliser une recherche par force brute pour retrouver le secret choisi par Alice.

p = 13
g = 6
Ka = 5

for a in range(1, p):
    if pow(g, a, p) == Ka:
        print(f"Brute force => Le secret choisi par Alice est: {a}")

print(f"------ 2.2 ------")
# Utiliser discrete_log de la librairie sympy.ntheory pour retrouver le secret choisi par Alice.

from sympy.ntheory import discrete_log

a = discrete_log(p, Ka, g)
print(f"Discret log => Le secret choisi par Alice est: {a}")

## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##
## -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ##

print(f"------ EXERCICE 3 : Attaque Man in the Middle ------")

# Alice et Bob partagent une clé par le protocole de Diffiee et Hellman.
# Ils ont choisi p = 17 et g = 3 comme générateur de (Z/17Z∗).
# Oscar a coupé la communication entre Alice et Bob et se fait passer pour Bob auprès d'Alice et pour
# Alice auprès de Bob. Il a choisi a = 7 pour communiquer avec Alice et b = 4 pour communiquer avec
# Bob.

print(f"------ 3.1 ------")
# Calculer la clé qu'il va transmettre à Alice qui pense recevoir cette clé de Bob.
# Calculer la clé qu'il va transmettre à Bob qui pense recevoir cette clé d'Alice.

p = 17
g = 3
a = 7
b = 4

Key_alice = pow(g, a, p)
Key_bob = pow(g, b, p)

print(f"Clé qu'Oscar transmet à Alice, se faisant passer pour Bob : {Key_bob}")
print(f"Clé qu'Oscar transmet à Bob, se faisant passer pour Alice : {Key_alice}")


print(f"------ 3.2 ------")
# Alice envoie Ka = 8 et Bob envoie Kb = 6.
# Calculer la clé que Oscar partagera avec Alice et la clé qu'il partagera avec Bob

Ka = 8
Kb = 6

Koa = pow(Ka, a, p)
Kob = pow(Kb, b, p)

print(f"Clé partagée entre Oscar et Alice: {Koa}")
print(f"Clé partagée entre Oscar et Bob: {Kob}")

print(f"------ 3.3 ------")
# Alice a utilisé sa clé (qu'elle pense partager avec Bob) pour envoyer un message à Bob.
# Elle utilise un chiffre de César:
# 'Hpaji Qdq rdbbt rdcktcj yt kxtch rwto idx stbpxc P igth kxit'
# Retrouver le message qu'elle a envoyé.
# En utilisant la clé que Bob pense partager avec Alice, retrouver le message que Bob a reçu (qui
# a peut-être été modifié par Oscar):
# 'Wepyx Fsf jmrepiqirx ni ri zmirw tew glid xsm hiqemr'
def cesar_dechiffrer(message, cle):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_dechiffre = ''

    cle = cle % 26

    for caractere in message:
        if caractere in alphabet:
            # Minuscule
            index = (alphabet.index(caractere) - cle) % 26
            message_dechiffre += alphabet[index]
        elif caractere in ALPHABET:
            # Majuscule
            index = (ALPHABET.index(caractere) - cle) % 26
            message_dechiffre += ALPHABET[index]
        else:
            # Espace ou autre caractère
            message_dechiffre += caractere
    return message_dechiffre


message_alice = 'Hpaji Qdq rdbbt rdcktcj yt kxtch rwto idx stbpxc P igth kxit'
cle_alice = Koa % 26
message_dechiffrer_alice = cesar_dechiffrer(message_alice, cle_alice)
print(f"Message envoyé par Alice: {message_dechiffrer_alice}")


message_bob = 'Wepyx Fsf jmrepiqirx ni ri zmirw tew glid xsm hiqemr'
cle_bob = Kob % 26
message_dechiffre_bob = cesar_dechiffrer(message_bob, cle_bob)
print(f"Message reçu par Bob: {message_dechiffre_bob}")

