# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:48:51 2020

@author: moism
"""
# Regresión con árboles de decisión
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Realizar la importación del dataset
dataset = pd.read_csv('Position_Salaries.csv')

#Selección de los datos a trabajar
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

# Ajustar la regresión con el dataset
from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor(random_state = 0)
regression.fit(X,y)

# Predicción de nuestros modelos
y_pred = regression.predict([[6.5]])


# Visulización de los resultados del Modelo Polinómico
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color="red")
plt.plot(X, regression.predict(X), color="blue")
plt.title("Modelo de Regresión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en ($)")
plt.show()








