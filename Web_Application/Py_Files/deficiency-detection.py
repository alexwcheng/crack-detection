import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
import pandas as pd
import requests
import json
import math
import sklearn
from scipy import stats
from scipy.stats import norm
from sklearn.utils import resample
import pickle
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
from wordcloud import WordCloud
import random
from collections import Counter
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, cross_val_score, cross_validate
from sklearn.linear_model import LassoCV, Lasso, Ridge, LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix, roc_auc_score, precision_recall_curve, precision_recall_fscore_support
import scipy.stats as stats
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE, ADASYN
from pprint import pprint
import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential, load_model, Input, Model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.utils import np_utils
from keras import backend, layers, models
from PIL import Image
import imageio
import os
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

st.title('Deficiency Detection')
st.header("This tool automatically identifies cracking in materials using Convolutional Neural Networks (CNNs).")
st.write("Please pick an image using the drop-down menu on the left.")

st.sidebar.title("Image Selection")

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/Users/alexandercheng/Desktop/Demo-Images/") if isfile(join("/Users/alexandercheng/Desktop/Demo-Images/", f))]
imageselect = st.sidebar.selectbox("Please pick an image using this drop-down menu.", onlyfiles)

image = Image.open("/Users/alexandercheng/Desktop/Demo-Images/" + imageselect)
st.image(image, use_column_width=True)

import General_Testing
import Material_Testing
import Crack_Testing

@st.cache
def General_Detection():
	model_1_path = '/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_general.h5'
	model_1 = load_model('/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_general.h5')
	return model_1

@st.cache
def Material_Detection():
	model_2_path = '/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_material_classification.h5'
	model_2 = load_model('/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_material_classification.h5')
	return model_2

@st.cache
def Crack_Detection():
	model_3_path = '/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_all.h5'
	model_3 = load_model('/Users/alexandercheng/Desktop/Deficiency-Detection-Web-Application/cnn_all.h5')
	return model_3


model_1 = General_Detection()
model_2 = Material_Detection()
model_3 = Crack_Detection()

prediction_1 = General_Testing.predict((model_1),"/Users/alexandercheng/Desktop/Demo-Images/" + imageselect)
st.subheader('Step 1:')
st.write('Is the image "General" or "Specific" ?')
st.title(prediction_1)

if prediction_1[1] == 'General':
	st.write('**This is just a general progress photo.**')
	st.write('**Nothing specific to detect.**')

elif prediction_1[1] == 'Specific':

	prediction_2 = Material_Testing.predict((model_2),"/Users/alexandercheng/Desktop/Demo-Images/" + imageselect)
	st.subheader('Step 2:')
	st.write('What is the material type?')
	st.title(prediction_2)

	prediction_3 = Crack_Testing.predict((model_3),"/Users/alexandercheng/Desktop/Demo-Images/" + imageselect)
	st.subheader('Step 3:')
	st.write('Is it "Cracked" Or "Not Cracked" ?')
	st.title(prediction_3)

	if float(prediction_3[0][0:3]) < 90:
		st.write('**PREDICTION IS LESS THAN 90% PROBABILITY.**')
		st.write('**PLEASE REVIEW IMAGE MANUALLY.**')
		st.title('😄')

else:
	pass




















