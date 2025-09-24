"""
How to plot and save a greyscale image.

The following example shows how to plot a 2-dimensional list of integers between 0 and 255 as a grayscale image.
Use these commands in mnist.py to generate an image of your average 3.
"""

from matplotlib import pyplot as plt
import mnist
from mnist_data import items
average_3 = mnist.average_digit(items,'label')

plt.imshow(average_3, cmap='gray_r')
plt.savefig('average_3.png')
