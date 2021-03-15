#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:16:58 2021

@author: mrent
"""

"""
    Redes Neuronales Artificiales

    Parte 1 - Preprocesado de los datos..
"""

# Realizar la importación de las librerías
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values


# Codificar datos categóricos
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columnTransformer = ColumnTransformer(
    transformers = [
        ('Geography', OneHotEncoder(drop='first'), [1]),
        ('Gender', OneHotEncoder(drop='first'),[2])],
    remainder="passthrough")
X = columnTransformer.fit_transform(X)



# Dividir el dataset en el conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


# Parte 2 - Realizar la construcción de la RNA
# Importar Keras y librerias adicionales
from keras.models import Sequential
from keras.layers import Dense

# Inicializar la RNA
classifier = Sequential()

# Añadir las capas de entrada y primera capa oculta de la red neuronal

# El número de nodos suele ser el promedio de la suma de los nodos de las variables independientes y dependientes.
classifier.add(Dense(units = 6, kernel_initializer="uniform", 
                     activation="relu", input_dim = 11))

# Añadir la segunda capa oculta
classifier.add(Dense(units = 6, kernel_initializer="uniform", activation="relu"))

# Añadir la capa de salida
classifier.add(Dense(units = 1, kernel_initializer="uniform", activation="sigmoid"))

# Compilar la RNA
classifier.compile(optimizer = "adam", loss = "binary_crossentropy", metrics=["accuracy"])

# Ajustamos la RNA al Conjunto de entrenamiento
classifier.fit(X_train, y_train, batch_size=10, epochs=10)


# Parte 3  - Evaluar el modelo y calcular predicciones finales

# Predicción de los resultados con el conjunto de testing
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Elaborar una matriz de confusión
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

















