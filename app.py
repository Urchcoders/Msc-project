import streamlit as st
import time
import numpy as np
from PIL import Image
import random 
import tensorflow as tf
from tensorflow.keras.models import load_model
from helper import predict_image

# import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing.image import img_to_array, load_img
# from keras.preprocessing.image import load_img

# Load your model here (replace 'model.h5' with your model file)
@st.cache_resource #(allow_output_mutation=True)
def load_keras_model():
    model = load_model('InceptionV3_softmax.h5')
    return model

model = load_keras_model()

# Title
st.title("Image Classification Interface")

# Image Upload
st.header("Upload or Drag-and-Drop Your Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    # Load the image using PIL
    image = Image.open(uploaded_file)
    
    # Display the image using Streamlit's st.image
    st.header("Preview of Uploaded Image")
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Save the uploaded image to a temporary file
    temp_file = f"temp_image.{uploaded_file.name.split('.')[-1]}"
    image.save(temp_file)
    
    # Convert image to array
    # image_array = img_to_array(image)
    # image_array = np.expand_dims(image_array, axis=0)  # Model expects batch dimension
    
    # Simulate a prediction delay
    if st.button("Predict"):
        with st.spinner('Making prediction...'):

            # time.sleep(1)
            print('hello')
             # Use the helper function to predict the class
            predicted_class = predict_image(temp_file, model)           

            st.success(f"Prediction: {predicted_class}")
