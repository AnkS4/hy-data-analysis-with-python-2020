#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    '''
    plt.subplot(1, 2, 1)
    plt.plot(a[:,0], a[:,1])
    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    '''
    plt.show()

def main():
    a = np.column_stack([[1, 2, 3], [2, 4, 6], [0.24, 2.99, -1.49], [25, 50, 10]])
    subfigures(a)

if __name__ == "__main__":
    main()
