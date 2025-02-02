#### shuffle the pixel position without changing pixel values
#### shuffling colum wise and row wise

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import display_img as di

### strenght of index lies in non-linearlity and randomness - strength the shuffling

### index generating function
def index_generator(x,r,n):
    index = []
    k = []

    for i in range(n):
        x = r*x*(1-x)  ### logastic map 
        k.append(x)   ### generated chaotic values append in list k
        index.append(i)  ### generating index

    for i in range(n):
        for j in range(n):
            if(k[i] > k[j]):
                ### arranging key in ascending order
                k[i], k[j] = k[j], k[i]

                ### re-arranging index as arrangement of its key
                index[i], index[j] = index[j], index[i]
    
    return index


### shuffling function-row-wise
def shuffling_img_row(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape

    index = index_generator(0.1, 3.91, height)

    shuffled_img = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            shuffled_img[i,j, :] = img[index[i] , j, :]
    return shuffled_img

### shuffling column-wise
def shuffling_img_col(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape

    index = index_generator(0.01, 3.89, width)

    shuffled_img = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            shuffled_img[i,j, :] = img[i , index[j], :]
    return shuffled_img


### reshuffling function for row-wise shuffled
def reshuffling_img_row(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape

    index = index_generator(0.1,3.91,height)
    reshuffled_img = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            reshuffled_img[index[i], j, :] = img[i, j, :]

    return reshuffled_img

### reshuffling function for column-wise shuffled
def reshuffling_img_col(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape
    index = index_generator(0.01, 3.89, width)
    reshuffled_img = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            reshuffled_img[i ,index[j], :] = img[i, j, :]

    return reshuffled_img


def shuffling(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape

    ### shuffling row-wise
    index = index_generator(0.1, 3.91, height)
    shuffled_img_row = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            shuffled_img_row[i,j, :] = img[index[i] , j, :]
    

    ### shuffling column_wise
    index = index_generator(0.01, 3.89, width)

    shuffled_img_col = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            shuffled_img_col[i,j, :] = shuffled_img_row[i , index[j], :]
        
    plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg', shuffled_img_col)
    return shuffled_img_col

def reshuffling(img_path):
    img = mpimg.imread(img_path)
    height, width, _ = img.shape

    ### reshuffling column-wise
    index = index_generator(0.01, 3.89, width)
    reshuffled_img_col = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            reshuffled_img_col[i ,index[j], :] = img[i, j, :]

    ### reshuffling row-wise
    index = index_generator(0.1,3.91,height)
    reshuffled_img_row = np.zeros_like(img, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            reshuffled_img_row[index[i], j, :] = reshuffled_img_col[i, j, :]

    plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\decrypted.jpg', reshuffled_img_row)
    return reshuffled_img_row

  
    

if __name__ =='__main__':
    # path = r'E:\PRODIGY_INTERN\PRODIGY_CS_02\image\luffy.jpeg'
   
    # ### shuffling pixels column-wise
    # shuffle_img_row = shuffling_img_row(path)
    # shuffle_img_col = shuffling_img_col(path)
    # plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg', shuffle_img_col)


    # ### Reshuffling the pixels
    # path_suff = r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg'
    # reshuffle_img_row = reshuffling_img_row(path_suff)
    # reshuffle_img_col = reshuffling_img_col(path_suff)
    # plt.imsave(r'E:\PRODIGY_INTERN\PRODIGY_CS_02\decrypted.jpg', reshuffle_img_col)


    path = r'E:\PRODIGY_INTERN\PRODIGY_CS_02\image\luffy.jpeg'
    path_suff = r'E:\PRODIGY_INTERN\PRODIGY_CS_02\encrypted.jpg'

    shuffle = shuffling(path)
    reshuffle = reshuffling(path_suff)

    ### display images
    di.show(path, shuffle,reshuffle)

