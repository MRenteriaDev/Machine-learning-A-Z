#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 01:07:45 2020

@author: mois
"""


# Regresión con bosques aleatorios

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


# Ajustar el modelo Random Forest con el dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state = 0)
regressor.fit(X, y)

# Predicción de nuestros datos con el modelo
y_pred = regressor.predict([[6.5]])

# Visualuización del entrenamiento con Random Forest
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Modelo de regresión con Random Forest")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en ($) dlls")
plt.show()
