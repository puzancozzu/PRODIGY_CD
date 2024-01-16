from caesar_cipher_algorithm import *


while(True):

    inputted_text = input("\n Enter a Text to be Encrypted/Decrypted : ")

    shift_value = int(input("\n Enter a shift_value for Encryption/Decryption : "))

    choice = int(input("\n 1: Encryption \n 2: Decryption  \n Enter Your Choice : " ))

    if choice == 1:

        en = encrypt(inputted_text, shift_value)
        print(f'\n Encrypted Text Using Caesar Cipher Encryption with shift value {shift_value} is : {en} \n\n')
    
    else:

        de = decrypt(inputted_text, shift_value)
        print(f'\n Decrypted Text Using Ceaser Cipher Decryption with shift value {shift_value} is : {de} \n\n')


    exit_value = input("Do you want to exit (y/n) : ")
    if exit_value == 'y':
        break
