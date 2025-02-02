#### Image encryption using substution metho
### using key_gen - logistic map - chaotic non linear key
## Generating chaotic keys -key value is function of image height and widht 
## -inital and control paramaters are constant

import key_gen
from display_img import show
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np 

### Encryption function
def symm_sub_enc(path):

    img = mpimg.imread(path)

    ## Generating chaotic keys
    height = img.shape[0]
    width =  img.shape[1]
    key = key_gen.keygen(0.1,3.95,height*width)
    # print(key)
    


    ## encritption-substitution with XOR
    z=0
    encrypt_img = np.zeros(shape=[height,width,3], dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            ### XORing pixel values with key
            encrypt_img[i,j] = img[i,j]^key[z]
            z+=1   
    
    ### Normalize pixel values to [0, 1] before saving
    encrypt_img_normalized = encrypt_img / 255.0
    # plt.imshow(encrypt_img_normalized)
    # plt.show()
    plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg', encrypt_img_normalized)
    return encrypt_img_normalized



#### function for decryption
def symm_sub_dec(path):
    encrpt_img = mpimg.imread(path)

    height = encrpt_img.shape[0]
    width =  encrpt_img.shape[1]
    key = key_gen.keygen(0.1,3.95,height*width)
    

    z = 0
    decrypt_img = np.zeros(shape=[height,width,3], dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            decrypt_img[i,j] = encrpt_img[i,j]^key[z]
            z+=1
    
    ### Normalize pixel values to [0, 1] before saving
    decrypt_img_normalized = decrypt_img / 255.0
    # plt.imshow(decrypt_img_normalized)
    # plt.show()
    plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\decrypted.jpg', decrypt_img_normalized)
    return decrypt_img_normalized
    
original_img_path = r"E:\PRODIGY_INTERN\PRODIGY_CS_02\image\luffy.jpeg"
encrypt = symm_sub_enc(original_img_path)
decrypt = symm_sub_dec(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg')
show(original_img_path,encrypt, decrypt)
