import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import time
from keras import backend as K

classes = ['Cracked', 'Not Cracked']

#Prediction Function
def predict(model, path):
    img = load_img(path, target_size=(256, 256))
    img = img_to_array(img)
    img = img/255
    img = np.expand_dims(img, axis=0)
    predict = model.predict(img)
    pred_name = classes[np.argmax(predict)]
    prediction = str(round(predict.max()*100, 2))
    return prediction + '%', pred_name

if __name__ == "__predict__":
    predict()