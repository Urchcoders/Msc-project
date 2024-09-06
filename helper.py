import tensorflow as tf
# from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import itertools

import os
import random
# import warnings



import numpy as np
def prepare_image(file):
  img = image.load_img(file, target_size=(224, 224))  # InceptionV3 input size
  img_array = image.img_to_array(img)
  img_array_expanded = np.expand_dims(img_array, axis=0)
  return tf.keras.applications.inception_v3.preprocess_input(img_array_expanded)



from tensorflow.keras.preprocessing import image

def predict_image(file,model):
  preprocessed_image = prepare_image(file)
  prediction = model.predict(preprocessed_image)
  # Assuming your model has two classes (e.g., 'NORMAL' and 'PNEUMONIA')
  class_labels = ['NORMAL', 'PNEUMONIA']
  predicted_class = class_labels[np.argmax(prediction)]
  return predicted_class
