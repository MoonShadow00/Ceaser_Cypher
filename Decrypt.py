alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def ceaser_decrypt(cyphertext, drift):
    result = ""

    for char in cyphertext.upper():
        if char in alphabet:

            old_index = alphabet.index(char)
            new_index = (old_index - drift) % len(alphabet)
            result += alphabet[new_index]

        else:
            result += char
    return result
