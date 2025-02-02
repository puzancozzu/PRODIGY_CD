def xor_decrypt(path, key):    
    try:
        
        path = path
        key = key
        
        fin = open(path, 'rb')
    
        image = fin.read()
        fin.close()
        
        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)
    
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        ## storing decrypted image in new image file
        fin = open("decrypted.jpg", 'wb')
        
        fin.write(image)
        fin.close()
        print('Decryption Done...')
    
    
    except Exception:
        print('Error caught : ', Exception.__name__)

def xor_encrypt(path, key):
    
    try:

        path = path
        
        key = key

        fin = open(path, 'rb')
    
        image = fin.read()
        fin.close()
        
        image = bytearray(image)
    
        for index, values in enumerate(image):
            image[index] = values ^ key
    
        fin = open("encrypted.jpg", 'wb')
        
        fin.write(image)
        fin.close()
        print('Encryption Done...')
        
    except Exception:
        print('Error caught : ', Exception.__name__)