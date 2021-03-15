# Regresión con uso de Random Forest

# Realizar la importación del dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

# Ajustar el modelo con Random Forest
install.packages("randomForest")
library(randomForest)
set.seed(123)
regression = randomForest(x = dataset[1],
                          y = dataset$Salary,
                          ntree = 10)

# Predicción de los resultados con Regresión
y_pred = predict(regression, newdata = data.frame(Level = 6.5))

# Visualización del aprendizaje del modelo
library(ggplot2)

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression,
                                               newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Predicción con Árbol de Decisión (Modelo de Regressión)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo en (en $)")