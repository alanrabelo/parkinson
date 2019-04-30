import numpy as np

# Plotting Library
import matplotlib.pyplot as plt

from scipy import misc
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import *

 
# FUNÇÕES MORFOLOGICAS
from skimage import morphology
from skimage.morphology import disk

disease_name = 'patient.jpg'
folha_color = imread(disease_name)
disease = rgb2gray(imread('patient.jpg'))

# Exibe imagens
fig = plt.figure(figsize=(20,20))
a = fig.add_subplot(1,4,1)
plt.imshow(disease, cmap=plt.cm.gray)
a.set_title('Original')
plt.axis('off')

open_3  = morphology.opening(disease, disk(3))
open_15 = morphology.opening(disease, disk(15))
difference = open_15 - disease
global_thresh = threshold_otsu(difference)
difference = difference > global_thresh


# Exibe imagens
fig = plt.figure(figsize=(10,10))
a = fig.add_subplot(1,4,1)
plt.imshow(disease, cmap=plt.cm.gray)
a.set_title('Original')
plt.axis('off')

a = fig.add_subplot(1,4,2)
plt.imshow(open_3, cmap=plt.cm.gray)
a.set_title('Abert (3)')
plt.axis('off')

a = fig.add_subplot(1,4,3)
plt.imshow(open_15, cmap=plt.cm.gray)
a.set_title('Abert (15)')
plt.axis('off')

a = fig.add_subplot(1,4,4)
plt.imshow(difference, cmap=plt.cm.gray)
a.set_title('Diferença')
plt.axis('off')

plt.tight_layout()
plt.show()

# Minha alteração