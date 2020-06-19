#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_red(img):
    img2 = img.copy()
    img2[:, :, (1,2)] = 0
    return img2

def to_green(img):
    img2 = img.copy()
    img2[:, :, (0,2)] = 0
    return img2

def to_blue(img):
    img2 = img.copy()
    img2[:, :, (0,1)] = 0
    return img2

def to_grayscale(img):
    img2 = img.copy()
    #w = np.array([0.2126, 0.7152, 0.0722]).reshape(1, 1, 3)
    #img2 = img2 * w
    img2 = 0.2126*img2[:, :, 0] + 0.7152*img2[:, :, 1] + 0.0722*img2[:, :, 2]
    return img2

def main():
    img = plt.imread("src/painting.png")
    gray = to_grayscale(img)
    plt.imshow(img)
    #plt.show()
    plt.imshow(gray, cmap="gray")
    #plt.show()
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(img))
    ax[1].imshow(to_green(img))
    ax[2].imshow(to_blue(img))
    plt.show()

if __name__ == "__main__":
    main()
