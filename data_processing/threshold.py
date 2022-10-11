'''
This code outputs the original image, grayscale image, the corresponding
histogram, removes the background and oberlays the background removed image on
top of the original images. This helps visualize whether the background removal
successfully retained particles that correspond with the glass particles in the
image.


Thresholding: https://datacarpentry.org/image-processing/07-thresholding/
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
image = skimage.io.imread("data/001.jpeg")
print(image.max()) #255 white
print(image.min()) #0 black
image = exposure.adjust_gamma(image, 1.5) # change brightness. greater than 1, darker. Less than 1, lighter

fig, ax = plt.subplots()
plt.imshow(image)
plt.show()

# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)


# blur the image to denoise
blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

fig, ax = plt.subplots()
plt.imshow(blurred_image, cmap="gray")
plt.show()

# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()

# gamma 1.5, threshold 0.15 

# # create a mask based on the threshold
t = 0.15
binary_mask = blurred_image > t #black rocks, white background. white rocks "< t"

# perform automatic thresholding
# t = skimage.filters.threshold_otsu(blurred_image)
# print("Found automatic threshold t = {}.".format(t))

# binary_mask = blurred_image > t
fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap="gray")
plt.show()

plt.imshow(image, cmap='gray')
plt.imshow(binary_mask, cmap='jet',alpha=0.5)
plt.show()