#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:02:31 2020

@author: mrdev

    #Natural Language Processing
"""

# Realizar las importación de las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Realizar la carga del dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter="\t", quoting=3)


# Realizar la limpieza del texto
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words("english") )]
    review = ' '.join(review)
    corpus.append(review)



# Se procede con la creación del back of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


# Dividir el dataset en conjunto de entrenamiento y de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=0)


# Ajustar el clasificador al conjunto de entrenamiento
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)


# Predicción de los resultados con el conjunto de Testing
y_pred = classifier.predict(X_test)


# Elaborar una matriz de confusión
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

