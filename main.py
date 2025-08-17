import sys
import Encrypt
import Decrypt
from Encrypt import encrypted
from Decrypt import decrypted

data = input("would you like to encrypt or decrypt? Leave blank to Terminate ")
if data == "encrypt":
    unencryptedtext = input("Enter encrypted message")
    driftvalue = int(input("Enter the number of drift in the ciphertext: "))
    print("Encrypted:", encrypted)
elif data == "decrypt":
    encryptedtext = input("Enter encrypted message")
    driftvalue = int(input("Enter the number of drift in the ciphertext: "))
    print("Decrypted:", decrypted)
elif data == "":
    print("Program Terminated")
    sys.exit(0)
