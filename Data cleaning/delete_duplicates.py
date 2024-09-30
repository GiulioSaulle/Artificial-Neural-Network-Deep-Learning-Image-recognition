import os
import hashlib
import numpy as np
from PIL import Image

# Defining the function to hash the images
def image_hash(image):
    return hashlib.md5(image).hexdigest()
	
# Load the dataset
dataset = np.load('public_data_cleanup.npz', allow_pickle=True)

# Initialize the needed variables
image_hashes = {}
remove_duplicates = []
data_array = dataset['data']
labels_array = dataset['labels']
index = 0

# Hash each image and add its index to the duplicates if it matches with another one
for file in data_array:
    hash_value = image_hash(file)
    
    if hash_value in image_hashes:
        remove_duplicates.append(index)
    else:
        image_hashes[hash_value] = file
    index += 1

# Removing the duplicated images and labels 
dataset_cleanup_img = np.delete(dataset['data'], remove_duplicates, axis=0)
dataset_cleanup_lbl = np.delete(dataset['labels'], remove_duplicates, axis=0)

# Creating the .npz file
np.savez_compressed('public_data_cleanup_no_duplicates.npz', data=dataset_cleanup_img, labels=dataset_cleanup_lbl)

