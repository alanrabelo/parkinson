# Importing Library
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import filters
from skimage import morphology
from skimage.morphology import square, rectangle, disk
from skimage.filters import threshold_otsu

# Importing Image
file_name = 'mea2-H2.jpg'
image = rgb2gray(imread(file_name))

open = morphology.opening(image, disk(15))
difference = open - image
global_thresh = threshold_otsu(difference)
difference = difference > global_thresh

# Plot Image
fig = plt.figure(figsize=(100, 100))

a = fig.add_subplot(1, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
a.set_title('Original')
plt.axis('off') 

a = fig.add_subplot(1, 2, 2)
plt.imshow(open, cmap=plt.cm.gray)
a.set_title('Abert')
plt.axis('off')

plt.show()
