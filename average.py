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
import pickle
from PIL import Image
import glob

# folders = ['Dataset/Healthy/HealthySpiral', 'Dataset/Patient/PatientSpiral']
folders = ['Dataset/Healthy/HealthySpiral',
           'Dataset/Healthy/HealthyMeander',
           'Dataset/Patient/PatientSpiral',
           'Dataset/Patient/PatientMeander'
           ]

healthy_filename = 'healthy.dict'
disease_filename = 'patient.dict'

try:
    healthy = pickle.load(open(healthy_filename, 'rb'))
    patient = pickle.load(open(disease_filename, 'rb'))
except:

    patient = {}
    healthy = {}

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

            if index >= 2:
                if patient_name in patient:
                    patient[patient_name].append(number_of_points_disease)
                else:
                    patient[patient_name] = [number_of_points_disease]
            else:
                if patient_name in healthy:
                    healthy[patient_name].append(number_of_points_disease)
                else:
                    healthy[patient_name] = [number_of_points_disease]


    with open(healthy_filename, 'wb') as f:
        pickle.dump(healthy, f)

    with open(disease_filename, 'wb') as f:
        pickle.dump(patient, f)


from matplotlib import pyplot as plt


dataset = []

for value in healthy.values():
    new_value = value
    new_value.append(0)
    dataset.append(new_value)

for value in patient.values():
    new_value = value
    new_value.append(1)
    dataset.append(new_value)



from sklearn.preprocessing import MinMaxScaler
import itertools

dataset = MinMaxScaler().fit_transform(dataset)

combinations = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7], 2))

dataset = np.array(dataset)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(dataset)
print(pca.explained_variance_ratio_)
new_array = []

for index,data in enumerate(dataset):
    new_data = list(principalComponents[index, :])
    new_data.append(data[-1])
    new_array.append(new_data)

for data in new_array:

    y = int(data[-1])
    if y == 0:
        plt.plot(data[0], data[1], 'bo')
    else:
        plt.plot(data[0], data[1], 'ro')

plt.show()



# for combination in combinations:
#
#     for value in dataset:
#
#         y = int(value[-1])
#         x1 = value[combination[0]]
#         x2 = value[combination[1]]
#
#         if y == 0:
#             plt.plot(x1, x2, 'bo')
#         else:
#             plt.plot(x1, x2, 'ro')
#
#     plt.show()
