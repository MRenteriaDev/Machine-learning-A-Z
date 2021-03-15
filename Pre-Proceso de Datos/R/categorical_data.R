# Importar el dataset
datasets = read.csv('../moises_ren/Moises/Cursos Udemy/Machine Learning A-Z/Mis Análisis/Pre-Proceso de Datos/Data.csv')


# Codificar las variables categóricas
datasets$Country = factor(datasets$Country,
                          levels = c("France", "Spain", "Germany"),
                          labels = c(1,2,3))

datasets$Purchased = factor(datasets$Purchased,
                            levels = c("No", "Yes"),
                            labels = c(0, 1))
