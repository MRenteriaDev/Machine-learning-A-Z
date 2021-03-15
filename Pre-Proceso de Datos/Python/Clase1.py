# -*- coding: utf-8 -*-
"""
Moisés Rentería

17 de mayo del 2020
"""

#Plantilla del Pre - Procesado de datos

# Realizar la importación de las líbrerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../Data.csv')

# Realizamos el retiro de la columna index
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# Codificación de los datos categóricos
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:, 0]  = le_X.fit_transform(X[:,0])




# Dividir el dataset en entrenamiento y testing
from sklearn.model_selection import train_test_split
# Se definen los modelos de evaluación y de entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



# Escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
# El escalado las variables se realizará igual que al trozo de datos de entrenamiento
X_test = sc_X.transform(X_test)"""







