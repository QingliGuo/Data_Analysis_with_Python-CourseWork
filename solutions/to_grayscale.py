#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    height, width = image.shape[0:2]
    weights = np.array ([0.2126, 0.7152, 0.0722 ]).reshape(1,1,3)
    new_image = image * weights
    grey_image = np.array([np.sum (new_image[i,j,:]) for i in range(height) for j in range(width) ]).reshape(height,width)
    return grey_image

def to_red(image):
    m = np.array([1,0,0]).reshape(1,1,3)
    return image * m
def to_green(image):
    m = np.array([0,1,0]).reshape(1,1,3)
    return image * m
def to_blue(image):
    m = np.array([0,0,1]).reshape(1,1,3)
    return image * m

def main():
    painting = plt.imread("src/painting.png")
    plt.imshow (painting)
    plt.show()

    plt.imshow(to_grayscale(painting),cmap='gray')
    plt.show()

    fig,ax = plt.subplots(3,1,figsize=(7,7))
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting))
    ax[2].imshow(to_blue(painting))
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
