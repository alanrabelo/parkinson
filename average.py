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

from PIL import Image
import glob

# folders = ['Dataset/Healthy/HealthySpiral', 'Dataset/Patient/PatientSpiral']
folders = ['Dataset/Healthy/HealthySpiral',
           'Dataset/Healthy/HealthyMeander',
           'Dataset/Patient/PatientSpiral',
           'Dataset/Patient/PatientMeander'
           ]

results = {'spiral' : {}, 'meander' : {}}

sum_of_points = [0, 0]
valores_healthy = []
valores_patient = []
acertos = [0, 0]
erros = [0, 0]

threshold = 51000

for index,folder in enumerate(folders):

    filenames = glob.glob(folder + '/*.jpg')
    for filename in filenames:

        patient_name = filename.split('/')[-1].split('-')[-1].split('.')[0]


        disease = rgb2gray(imread(filename))

        open_15 = morphology.opening(disease, disk(15))
        difference = open_15 - disease
        global_thresh = threshold_otsu(difference)
        difference = difference > global_thresh

        # bw_disease_thresh = threshold_otsu(disease)
        # bw_disease_image = disease < bw_disease_thresh
        #
        # disease_hole_filled = binary_fill_holes(bw_disease_image)

        number_of_points_disease = sum(sum(difference))

        if index == 0:

            valores_healthy.append(number_of_points_disease)
            if number_of_points_disease < threshold:
                acertos[index] += 1
            else:
                erros[index] += 1


        if index == 1:

            valores_patient.append(number_of_points_disease)

            if number_of_points_disease > threshold:
                acertos[index] += 1
            else:
                erros[index] += 1


        sum_of_points[index] += number_of_points_disease

    sum_of_points[index] /= len(filenames)


# Plotando as somas dos pontos

from matplotlib import pyplot as plt

valores_patient = np.array(valores_patient)

valores_patient = valores_patient[valores_patient>=370000]

valores_healthy = np.array(valores_healthy)

valores_healthy = valores_healthy[valores_healthy>=370000]

plt.plot(valores_patient, 'o')
plt.plot(valores_healthy, 'o')
plt.show()
