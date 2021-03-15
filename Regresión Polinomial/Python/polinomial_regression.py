#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:09:11 2020

@author: moisesren
"""


# Regresión polinómica

#Realizar la importación de las librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importar el dataset
dataset = pd.read_csv('./Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# En la regresión polińomica no se realiza la división en este caso por que son pocos datos y poder seguir aprovechando los datos poco lineales
# Realizar la division del dataset en el conjunto de entrenamiento y de test
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 2 , random_state = 0)

# Ajustar la regresión lineal con el datasets

from sklearn.linear_model import LinearRegression
lin_reg= LinearRegression()
lin_reg.fit(X, y)



# Ajustar la regresión polinómica con el dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)


# Visualizar los datos del modelo lineal
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")
plt.title("Modelo de Regresión Lineal")
plt.xlabel("Nivel del empleado")
plt.ylabel("Sueldo en $(dolares)")
plt.show()

# Visualizar los datos del modelo polinomico
X_grid = np.arange(min(X),max(X), 0.1 )
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg2.predict(X_poly), color="blue")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Nivel del empleado")
plt.ylabel("Sueldo en $(dolares)")  
plt.show()

# Predicción de nuestros modelos
lin_reg.predict(np.array(6.5).reshape(1,1))
lin_reg2.predict(poly_reg.fit_transform(np.array(6.5).reshape(1,1)))