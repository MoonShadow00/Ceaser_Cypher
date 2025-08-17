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

plaintext = input()
drift = int(input())
encrypted = ceaser_cypher(plaintext, drift)
print("Encrypted:", encrypted)
