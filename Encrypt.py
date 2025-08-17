alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def ceaser_encrypt(plaintext, drift):
    result = ""

    for char in plaintext.upper():
        if char in alphabet:

            old_index = alphabet.index(char)
            new_index = (old_index + drift) % len(alphabet)
            result += alphabet[new_index]

        else:
            result += char
    return result


