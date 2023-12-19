import cv2
import os
import tensorflow as tf
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

data_dir = 'E:\\University\\FYP Stuff\\Dataset\\mst-e_data\\mst-e_image_details.csv'
df = pd.read_csv(data_dir)

data = []
labels = []

for index, row in df.iterrows():
    image_path = os.path.join(row['subject_name'], row['image_ID'])
    image = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if image is not None:
        data.append(image)
        labels.append(row['MST'])
    else:
        print(f"Error loading image: {image_path}")

data = np.array(data)
labels = np.array(labels)