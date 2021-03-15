# Plantilla para el preprocesado de datos


# Importar el dataset
datasets = read.csv('../moises_ren/Moises/Cursos Udemy/Machine Learning A-Z/Mis Análisis/Pre-Proceso de Datos/Data.csv')


# Dividir los datos en entrenamiento y en  el conjunto de test
library(caTools)
set.seed(123)
split = sample.split(datasets$Purchased, SplitRatio = 0.8)
training_set = subset(datasets, split == TRUE)
testing_set = subset(datasets, split == FALSE)

# Escalado de los valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])




