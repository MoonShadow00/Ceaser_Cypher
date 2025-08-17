import main
from main import encryptedtext,driftvalue

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def ceaser_cypher(cyphertext, drift):
    result = ""

    for char in cyphertext.upper():
        if char in alphabet:

            old_index = alphabet.index(char)
            new_index = (old_index - drift) % len(alphabet)
            result += alphabet[new_index]

        else:
            result += char
    return result

cyphertext = encryptedtext
drift = driftvalue
decrypted = ceaser_cypher(cyphertext, drift)
