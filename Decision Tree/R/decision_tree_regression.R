# Árbol de regresión para la decisión

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]


# Ajustar el modelo de la regresión con el conjunto de Datos
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))

# Predicción de nuevos resultados con árbol de regresión
y_pred = predict(regression, newdata = data.frame(Level = 6.5))

# Visualización del modelo del árbol de regresión

library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression,
                                               newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Predicción con Árbol de Decisión (Modelo de Regressión)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en (en $)")
