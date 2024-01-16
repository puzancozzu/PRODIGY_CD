#### ------------------------------------------------ CEASER CHIPER ALGORITHM --------------------------------------------------------------------------------------

#### We can Implement Caesar Cipher by manipulation the ASCII values
### Encryption = ( ASCII value of Char + shift value ) mod 26 --- mod 26 as after "Z" must continued from "A" again

### ord() --- change character to corresponding ASCII- integer value
### chr() --- change ASCII-int value to corresponding Character


### ---------------------------------------------------------------------------------------------------------------------------------------------------------


### FUNCTION FOR ENCRYPTION 
def encrypt(text_to_encrypt, shfit_value):

    encrypted_text = ""

    for letter in text_to_encrypt: 

        ## for Lowercase characters  a = 97 (ASCII)
        if (letter.islower()):
            
            encrypted_text = encrypted_text + chr((ord(letter) + shfit_value - 97) % 26 + 97)
 
        ## for uppercase characters A = 65
        else:
            encrypted_text += chr((ord(letter) + shfit_value - 65) % 26 + 65)

    return(encrypted_text)
 


### FUNCTION FOR DECRYPTION   
def decrypt(text_to_decrypt, shift_value):

    decrypted_text = ""

    for letter in text_to_decrypt:

        if (letter.isupper()):
            decrypted_text += chr((ord(letter) - shift_value - 65) % 26 + 65)

        else:
            decrypted_text += chr((ord(letter) - shift_value - 97) % 26 + 97)

    return(decrypted_text)




# inputted_text = input("Enter a Text to Encrypt : ")
# shift_value = int(input("Enter a shift_value for Encryption : "))
# en = encrypt(inputted_text, shift_value)
# print(f'Encrypted Text Using Caesar Cipher Encryption with shift value {shift_value} is : {en}')