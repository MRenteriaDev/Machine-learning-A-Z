#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:44:43 2020

@author: moises_ren
"""

# Datos faltantes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../Data.csv')

# Realizamos el retiro de la columna index
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Empezar con el remplazo por la media
from sklearn.impute import SimpleImputer
# Reemplazar por medias
imputer = SimpleImputer(missing_values=np.NaN,strategy="mean", verbose=0)
# medias en columnas 1,2
imputer = imputer.fit(X[:, 1:3])
# Cambiar valores por dichas nedias
X[:, 1:3] = imputer.transform(X[:, 1:3])
