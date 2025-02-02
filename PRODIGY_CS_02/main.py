from xor_en_dc import *

path = input("Enter the path of image: ")
key = int(input("\n(encryption_key = decryptionkey) Enter a key value :"))

print("Enter Your Choice: \n")
choice = int(input("1. Encryption \n2. Decryption \n"))


if choice == 1:
    xor_encrypt(path, key)
else:
    xor_decrypt(path, key)

