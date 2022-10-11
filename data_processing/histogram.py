'''
This code outputs the histogram of the input image
'''

import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt

# read the image as grayscale from the outset
image = im.imread('001.jpeg')
x=image[:,:,0]

# display the image
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
plt.title("Original Image")
plt.imshow(x, cmap="gray")
plt.show()

# output histogram
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
plt.hist(x)
plt.show()