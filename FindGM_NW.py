
import tensorflow as tf
import keras
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import pytesseract
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from CheckApp import find_coordinates,search

def FindGM(image_path): #ResNet50
    img = image.load_img(image_path,target_size=(224,224))
    model = tf.keras.applications.resnet50.ResNet50()  # Сверточная НС
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    for classname in ['web_site','screen']:
        if classname in decode_predictions(prediction,top=3)[0][0]:
            return find_coordinates(search(image_path))
        else:
            pass

def FindGM2(image_path): #MobileNet
    MODEL = keras.models.load_model('modelGM_mobilenet.h5')
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array)
    prediction = MODEL.predict(img_preprocessed)
    print(prediction)
    if prediction[0][0] > 0.75 or prediction[0][0] > prediction[0][1]:
        return True

def FindGM3(image_path): #VGG19 Переобучение
    MODEL = keras.models.load_model('modelGM_VGG.h5')
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array)
    prediction = MODEL.predict(img_preprocessed)
    print(prediction)
    if prediction[0][0] > 0.75 or prediction[0][0] > prediction[0][1]:
        return find_coordinates(search(image_path)), True
        # return True