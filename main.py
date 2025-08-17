import sys
from Encrypt import ceaser_encrypt
from Decrypt import ceaser_decrypt

while True:
    data = input("would you like to encrypt or decrypt? Leave blank to Terminate ")

    if data.lower() == "encrypt":
        unencryptedtext = input("Enter encrypted message")
        driftvalue = int(input("Enter the number of drift in the ciphertext: "))
        result = ceaser_encrypt(unencryptedtext, driftvalue)
        print("Encrypted:", result)
    elif data == "decrypt":
        encryptedtext = input("Enter encrypted message")
        driftvalue = int(input("Enter the number of drift in the ciphertext: "))
        result = ceaser_decrypt(encryptedtext, driftvalue)
        print("Decrypted:", result)
    elif data == "":
        print("Program Terminated")
        sys.exit(0)
    else:
        print("Invalid Input")
        sys.exit(1)