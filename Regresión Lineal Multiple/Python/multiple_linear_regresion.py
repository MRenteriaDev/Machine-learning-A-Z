#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:29:25 2020

@author: moisesren
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('./50_Startups.csv')

# Realizamos el retiro de la columna index
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Importar las librerías para la codificación
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer

# Realizar la codificación de las columnas e 
# indicar la columna que desea pasar a variable dummy
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories="auto"), [3])],
    remainder = "passthrough"
)
X = np.array(ct.fit_transform(X), dtype=np.float)

# Evitar la trampa de las variables Dummys
X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Ajustar el modelo de Regresión Lineal Múltiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predicción de los resultados en el conjunto de testing
y_pred = regression.predict(X_test)

# Construir el modelo de RLM utilizando la Eliminación hacía atrás
import statsmodels.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X,axis=1)
SL = 0.05

#Generamos una matriz de características óptimas
#X_opt = X[:, [0,1,2,3,4,5]].tolist()
#regression_OLS = sm.OLS( y, X_opt).fit()
#regression_OLS.summary()

def backWardElimination(x, SL):
    numVars= len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x.tolist()).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > 1:
            for j in range(0, numVars - i):
                if(regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j,1)
                    tmp_regressor = sm.OLS(x, y.tolist()).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if(adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print(regressor_OLS.summary())
                        return x_rollback
                    else :
                        continue
    regressor_OLS.summary()
    return x

SL = 0.05
X_opt = X[:, [1,2,3,4,5]]
X_Modeled = backWardElimination(X_opt, SL)















