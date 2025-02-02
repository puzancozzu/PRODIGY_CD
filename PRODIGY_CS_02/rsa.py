import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import display_img as di

def reshuffling(img_path, key):
    path = img_path
    p, q = key
        
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()