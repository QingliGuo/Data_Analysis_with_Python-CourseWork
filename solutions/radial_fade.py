#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    image = a
    height, width = image.shape[:2]
    return ((height - 1) / 2, (width - 1) / 2)   # note the order: (center_y, center_x)

def radial_distance(a):
    image = a
    height, width = image.shape[:2]
    h, w = center(image)
    dist = np.array ([np.sqrt((h-i)**2 + (w-j)**2) for i in range(height) for j in range(width)]).reshape (height,width)
    return dist

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""

    max_d = np.max(a)
    min_d = np.min(a)
    if max_d == min_d:
        return 1 - (a-min_d)
    else:
        return 1 - (a - min_d)/(max_d - min_d)

def radial_mask(a):
    image = a
    distance = radial_distance(image)
    scaled_dist = scale (distance)
    return scaled_dist

def radial_fade(a):
    image = a
    height, width = image.shape[:2]
    masked = radial_mask (image)
    m = masked.reshape(height,width,1)
    return image * m

def main():
    painting = plt.imread ("src/painting.png")
    masked = radial_mask (painting)
    faded = radial_fade (painting)

    fig, ax = plt.subplots(3,1,figsize = (7,7))
    ax[0].imshow(painting)
    ax[1].imshow(masked,cmap='gray')
    ax[2].imshow(faded)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
