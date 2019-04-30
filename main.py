import numpy as np

# Plotting Library
import matplotlib.pyplot as plt

from scipy import misc
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import *
from scipy.ndimage.morphology import binary_fill_holes

 
# FUNÇÕES MORFOLOGICAS
from skimage import morphology
from skimage.morphology import disk

disease_name = 'healthy.jpg'
disease = rgb2gray(imread(disease_name))

healthy_name = 'healthy.jpg'
healthy = rgb2gray(imread(healthy_name))

open_15 = morphology.opening(disease, disk(15))
difference = open_15 - disease
global_thresh = threshold_otsu(difference)
difference = difference > global_thresh

bw_thresh = threshold_otsu(disease)
bw_image = disease < bw_thresh

hole_filled = binary_fill_holes(bw_image)


# Exibe imagens
fig = plt.figure(figsize=(10,10))
a = fig.add_subplot(2,2,1)
plt.imshow(disease, cmap=plt.cm.gray)
a.set_title('Original')
plt.axis('off')

a = fig.add_subplot(2,2,2)
plt.imshow(hole_filled, cmap=plt.cm.gray)
a.set_title('Preenchimento de buracos')
plt.axis('off')

a = fig.add_subplot(2,2,3)
plt.imshow(open_15, cmap=plt.cm.gray)
a.set_title('Abert (15)')
plt.axis('off')

a = fig.add_subplot(2,2,4)
plt.imshow(difference, cmap=plt.cm.gray)
a.set_title('Diferença')
plt.axis('off')

plt.tight_layout()
plt.show()

# Minha alteração

# TODO: Porcertatem de acerto: Porcentagem da linha que o desenho foi bom / ruim
# TODO: Testar as mesmas para os meanders
# TODO: Testar com círculos a área dos buracos / área pintada