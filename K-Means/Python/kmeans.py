#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:25:12 2020

@author: moises

K-Means
"""



# Importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Se realiza la  importación del dataset
dataset = pd.read_csv('./Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

# Método del codo para evaluar el número  óptimo de clusters
from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters= i, init="k-means++", max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    # El parámetro intertia nos da la suma de los cuadrados de la distancia
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.title("Método del codo")
plt.xlabel("Número de Clústers")
plt.ylabel("WCSS(k)")
plt.show()


# Aplicar el método de k-means para segmentar el dataset
kmeans = KMeans(n_clusters=5, init="k-means++", max_iter=300, n_init=10, random_state=0)
y_means = kmeans.fit_predict(X)

# Visualizar los clusters
plt.scatter(X[y_means == 0, 0], X[y_means==0,1], s=100, c='red', label="Cluster 1")
plt.scatter(X[y_means == 1, 0], X[y_means==1,1], s=100, c='blue', label="Cluster 2")
plt.scatter(X[y_means == 2, 0], X[y_means==2,1], s=100, c='green', label="Cluster 3")
plt.scatter(X[y_means == 3, 0], X[y_means==3,1], s=100, c='magenta', label="Cluster 4")
plt.scatter(X[y_means == 4, 0], X[y_means==4,1], s=100, c='cyan', label="Cluster 5")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300,c='black', label="varicentros")
plt.title("Clúster de clientes")
plt.xlabel("Ingresos anuales (en miles de $)")
plt.ylabel("Puntuación de gastos")
plt.legend()
plt.show()









