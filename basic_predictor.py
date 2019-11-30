"""
Written by Anthony Luo for ECOR 1052.
Originally written on google Colab, compiled by Google Colab.

Uses pretrained model and weights from basic_classification.
"""

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Flatten, Activation, Dense, Dropout, BatchNormalization, MaxPooling2D, Conv2D
from tensorflow.keras.preprocessing import image
from tensorflow.keras.callbacks import ModelCheckpoint
#from google.colab import drive
import numpy as np
import time
import h5py
import os

# filepaths
model_path = 'model/final_model.hdf5'
weights_path = 'model/final_weights.hdf5'

model = load_model(model_path)
model.load_weights(weights_path)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

def predictOnImage(img_path):
    pred_img = image.load_img(img_path.value, target_size = (128, 128))
    pred_img = image.img_to_array(pred_img)
    pred_img = np.expand_dims(pred_img, axis = 0)
    result = model.predict_classes(image)
    return int(result[0])

if __name__ == '__main__':
    paths = input('please enter a filepath to classify image on: ')
    predictOnImage(paths)