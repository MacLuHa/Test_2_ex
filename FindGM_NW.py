import tensorflow as tf
import keras
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from CheckApp import find_coordinates,search

def FindGM(image_path): #ResNet50
    #Загружаем изображение размером 224х224 для лучшей обработки
    img = image.load_img(image_path,target_size=(224,224))
    # Сверточная НС, дальше будем использовать обученные на исходном датасете модели
    model = tf.keras.applications.resnet50.ResNet50()
    #Создаем пакет из одного изображения
    img_array = image.img_to_array(img)
    #Увеличиваем количество измерений
    img_batch = np.expand_dims(img_array, axis=0)
    #Нормализуем каждый пиксель
    img_preprocessed = preprocess_input(img_batch)
    #И обучаем модель
    prediction = model.predict(img_preprocessed)
    #Здесь решил попробовать уже готовую модель
    for classname in ['web_site','screen']:
        if classname in decode_predictions(prediction,top=3)[0][0]:
            return True
        else:
            pass

def FindGM2(image_path): #MobileNet
    #Загружаем обученную на нужном датасете модель и повторяем процедуру
    MODEL = keras.models.load_model('modelGM_mobilenet.h5')
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array)
    prediction = MODEL.predict(img_preprocessed)
    print(prediction)
    #Если вероятность того, что это нужный класс больше 0.75
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
        return True

