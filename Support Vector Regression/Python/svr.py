# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:42:38 2020

@author: moism
"""

# Cómo importar las librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importar el dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Realizar el escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y= sc_y.fit_transform(y.reshape(-1,1 ))

# Ajustar la regresión con el dataset
from sklearn.svm import SVR
regression = SVR(kernel = "rbf")
regression.fit(X, y)


# Predicción de nuestros modelos con SVR
y_pred = regression.predict(sc_X.transform(np.array(6.5).reshape(1, -1)))
y_pred = sc_y.inverse_transform(y_pred)


#Visualización de los resultados del SVR
#X_grid = np.arange(min(X), max(X), 0.1)
#X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,y, color="red")
plt.plot(X, regression.predict(X),color="blue")
plt.title("Modelo de regresión SVR")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()