'''
This code outputs the original image, grayscale image, and the corresponding
histogram.
'''

import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
from skimage import data, img_as_float
from skimage import exposure

# load the image
image = skimage.io.imread("data_test/001.jpeg")
image = exposure.adjust_gamma(image, 1) # change brightness. greater than 1, darker. Less than 1, lighter

fig, ax = plt.subplots()
plt.imshow(image)
plt.show()

# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)

fig, ax = plt.subplots()
plt.imshow(gray_image, cmap="gray")
plt.show()


# # blur the image to denoise
# blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

# fig, ax = plt.subplots()
# plt.imshow(blurred_image, cmap="gray")
# plt.show()

# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(gray_image, bins=256, range=(0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()
