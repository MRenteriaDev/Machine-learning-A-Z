#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:44:31 2020

@author: moises_ren
"""

# Datos categóricos

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../Data.csv')

# Realizamos el retiro de la columna index
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Importar las librerías para la codificación
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer

# Realizar la codificación de las columnas e 
# indicar la columna que desea pasar a variable dummy
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories="auto"), [0])],
    remainder = "passthrough"
)
X = np.array(ct.fit_transform(X), dtype=np.float)
labelencoder_y = preprocessing.LabelEncoder()
y = labelencoder_y.fit_transform(y)