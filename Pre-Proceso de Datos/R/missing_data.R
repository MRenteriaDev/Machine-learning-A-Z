# Importar el dataset
datasets = read.csv('../moises_ren/Moises/Cursos Udemy/Machine Learning A-Z/Mis Análisis/Pre-Proceso de Datos/Data.csv')

# Tratamiento de los valores N/A
datasets$Age = ifelse(is.na(datasets$Age), 
                      ave(datasets$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      datasets$Age)

datasets$Salary = ifelse(is.na(datasets$Salary), 
                         ave(datasets$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                         datasets$Salary)
