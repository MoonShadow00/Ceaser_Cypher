import main
from main import unencryptedtext,driftvalue

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def ceaser_cypher(plaintext, drift):
    result = ""

    for char in plaintext.upper():
        if char in alphabet:

            old_index = alphabet.index(char)
            new_index = (old_index + drift) % len(alphabet)
            result += alphabet[new_index]

        else:
            result += char
    return result

plaintext = unencryptedtext
drift = driftvalue
encrypted = ceaser_cypher(plaintext, drift)

