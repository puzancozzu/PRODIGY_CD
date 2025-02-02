import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show(path,encrypt,decrypt):
    original_img = mpimg.imread(path)
    encrypted_img = encrypt
    decrypted_img = decrypt

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(original_img)
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(encrypted_img)
    plt.title('Encrypted Image')

    plt.subplot(1, 3, 3)
    plt.imshow(decrypted_img)
    plt.title('Decrypted Image')

    plt.show()