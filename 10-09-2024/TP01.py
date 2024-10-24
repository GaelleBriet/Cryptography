#import re
#import struct
import binascii
#from pydoc import plaintext

#from encodings.hex_codec import hex_decode, hex_encode

######## 1. Encodage ########

## 1.1. Décoder le message b'd\xc3\xa9cod\xc3\xa9!'
message = b'cd\xc3\xa9cod\xc3\xa9!'
decoded_message = message.decode('utf-8')
print(decoded_message)

## 1.2.
## - Écrire une fonction qui traduit un message en ascii (ou UTF-8)
## Exemple: 'hello' devient 104 101 108 108 111
def convert_to_ascii(message1):
    ascii_list = []
    for char in message1:
        coded_char = str(ord(char))
        ascii_list.append(coded_char)
    ascii_message = ' '.join(ascii_list)
    print(ascii_message)

message1 = 'hello'
convert_to_ascii(message1)

## - Écrire une fonction qui décode un message encodé UTF-8 et décoder le message suivant:
## 66 114 97 118 111 44 32 116 111 117 116 32 118 97 32 98 105 101 110 33
decoded = []

def decode_message(message2):
    numbers = message2.split()
    for number in numbers:
        decoded.append(chr(int(number)))
        decoded_message = ''.join(decoded)

    print(decoded_message)

message2 = "66 114 97 118 111 44 32 116 111 117 116 32 118 97 32 98 105 101 110 33"
decode_message(message2)

## 1.3.
## Écrire une fonction qui encode un message en binaire: chaque caractère est codé sur 8 bits.
## Exemple: 'hello' devient 0110100001100101011011000110110001101111

def encode_to_binary(message):
    binary_message = ""
    for char in message:
        # convert letter in ascii code
        ascii = ord(char)
        # convert in binary and format in 8bits
        binary_char = bin(ascii)[2:].zfill(8)
        # add to binary_message
        binary_message += binary_char
    return binary_message
print(encode_to_binary('hello'))

### Version avec binascii
def encode_to_binary_2(message):
    # convert message in bytes
    byte_message = binascii.a2b_qp(message)
    # convert bytes in binary 8bits
    binary_message = ''.join(format(byte, '08b') for byte in byte_message)
    return binary_message

print(encode_to_binary_2('hello'))


##- Écrire une fonction qui décode un message binaire et décoder le message suivant:
## 010001010111010000100000011101100110111101101001011011000110000100100001
def decode_binary_messsage(message):
    decoded_message = ""
    for i in range(0, len(message), 8):
        # extract 8bits group
        byte = message[i:i+8]
        # convert group into number
        number = int(byte, 2)
        # convert number into char
        char = chr(number)
        decoded_message += char
    return decoded_message

print(decode_binary_messsage('010001010111010000100000011101100110111101101001011011000110000100100001'))


## 1.4.
## Écrire une fonction qui encode un message en hexadécimal.
## Exemple: 'hello world' devient 68656C6C6F20776F726C64
def encode_to_hexadecimal(message):
    return message.encode('utf-8').hex().upper()

print(encode_to_hexadecimal('hello world'))


## Écrire une fonction qui décode et décoder le message: 53616C7574206C6573206861636B65727321
def decode_hex_to_string(hex):
    byte_string = binascii.unhexlify(hex)
    return byte_string.decode('utf-8')

print(decode_hex_to_string('53616C7574206C6573206861636B65727321'))

## 1.5.
## Utiliser la librairie python base64 pour écrire une fonction qui encode un message en base64.
## Exemple: 'Hello world!' devient SGVsbG8gd29ybGQh

def encode_message_in_base64(message):
    # convert message into bytes
    message_bytes = message.encode('utf-8')
    # encode to base64 (base64 needs bytes)
    base64_bytes = binascii.b2a_base64(message_bytes)
    # convert result (in bytes) into string
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

print(encode_message_in_base64('Hello world!'))

######## ######## ######## ########
######## 2. Chiffrement par substitution: chiffre ROT47 ########

## Écrire une fonction encryptROT47(plaintext) qui chiffre ou déchiffre en ROT47.
## Déchiffrer le message: 'y6 DF:D #~%cfi ;6 E@FC?6 DFC hc 42C24E6C6DP'

def encryptROT47(message):
    result = []
    for char in message:
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:
            result.append(chr(33 + ((ascii_val + 14) % 94)))
        else:
            result.append(char)
    return ''.join(result)

encrypted_mess = 'y6 DF:D #~%cfi ;6 E@FC?6 DFC hc 42C24E6C6DP'
decrypted_mess = encryptROT47(encrypted_mess)
print('message chiffré : ', encrypted_mess)
print('message déchiffré :', decrypted_mess)



######## ######## ######## ########
######## 3. DES-AES ########

## 3.1. Utiliser la librairie PyCryptodome pour déchiffrer le message suivant chiffré en simple DES avec
## le mode CBC, la clé b'8bytes k' et le vecteur d'initialisation b'\xcb\xb3\xc9p~\x027\xc9'

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

key = b'8bytes k'
init_vector = b'\xcb\xb3\xc9p~\x027\xc9'
message = b'\xf7;\\\xff\xd7yg\xe6\x02P\x0f\xdd\x1b\xeb\xec\xe5'

def decrypt_DES_CBC(key, init_vector, message):
    cipher = DES.new(key, DES.MODE_CBC, init_vector)
    decrypted_message = cipher.decrypt(message)
    return unpad(decrypted_message, DES.block_size).decode('utf-8')

print(decrypt_DES_CBC(key, init_vector, message))

## 3.2.  Déchiffrer le message suivant chiffré avec l'AES en mode GCM avec la clé b'super grande cle'
## et le nonce b'cn\xcd\x1d\xab\xff?\xd3OK\x96z'

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad

key = b'super grande cle'
nonce = b'cn\xcd\x1d\xab\xff?\xd3OK\x96z'
message = b')\x08\x87\xc3/\x18\x11\x83%\xa3`\xf8\xd6\xa6\x88\xa2@f$\xce\xad\x89\xf4'

def decrypt_AES_GCM(key, nonce, message):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt(message)
    return plaintext.decode('utf-8')
print(decrypt_AES_GCM(key, nonce, message))

