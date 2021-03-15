#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:34:05 2020

@author: moises
"""

# Clustering Jerárquico

# Importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
dataset = pd.read_csv('./Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

# Utilizar el dendograma para encontrar el número óptimo de clusters

import scipy.cluster.hierarchy as sch

"""
    el metodo ward intenta minimzar la varianza que existe entre los puntos
    que hay entre los clusters
"""
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrograma")
plt.xlabel("Clientes")
plt.ylabel("Distancia Euclidia")
plt.show()


# Ajustar el clustering a nuestro conjunto de datos
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")  
y_hc = hc.fit_predict(X)


# Visualización de los clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc==0,1], s=100, c='red', label="Cluster 1")
plt.scatter(X[y_hc == 1, 0], X[y_hc==1,1], s=100, c='blue', label="Cluster 2")
plt.scatter(X[y_hc == 2, 0], X[y_hc==2,1], s=100, c='green', label="Cluster 3")
plt.scatter(X[y_hc == 3, 0], X[y_hc==3,1], s=100, c='magenta', label="Cluster 4")
plt.scatter(X[y_hc == 4, 0], X[y_hc==4,1], s=100, c='cyan', label="Cluster 5")
plt.title("Clúster de clientes")
plt.xlabel("Ingresos anuales (en miles de $)")
plt.ylabel("Puntuación de gastos")
plt.legend()
plt.show()














