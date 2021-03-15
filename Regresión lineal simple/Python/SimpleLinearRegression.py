#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:24:21 2020

@author: moisesren
"""
# Realizar la importación de las líbrerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')

# Realizamos el retiro de la columna index
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Dividir el dataset en entrenamienro y test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Importar la clase de la regresión lineal
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train, sample_weight=None)

# Predecir con el conjunto de test
y_pred = regression.predict(X_test)

# Visualizar los datos del entrenamiento
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regression.predict(X_train), color= "blue")
plt.title("Sueldo vs Años de Experiencia, (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Aumentos de Salario en Dlls")
plt.show()

# Visualizar los datos del test
plt.scatter(X_test, y_test, color="red")
# Cómo los regresores ya se entrenaron en el conjunto de entrenamiento en el plot
# se matiene el X_train ya que la recta sigue siendo la misma
plt.plot(X_train, regression.predict(X_train), color= "blue")
plt.title("Sueldo vs Años de Experiencia, (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Aumentos de Salario en Dlls")
plt.show()