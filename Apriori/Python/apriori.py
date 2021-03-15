#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:41:47 2020

@author: moises

Regla de Asosiación Apriori --> Optimizado de Ventas
"""

# Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Se carga el dataset
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)

transactions = []

for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Entrenar el algoritmo de apriori
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, 
                min_lift = 3, min_length = 2)

# Visualización de los resultados
resulsts = list(rules)

resulsts[1]