# Regression polinómica

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio=0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)

# Ajustar el modelo de regresión lineal con el conjunto de datos
lin_reg = lm(formula = Salary ~ . ,
             data = dataset)

# Ajustar el modelo de polinomica lineal con el conjunto de datos
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula= Salary ~ . ,
              data = dataset)

# Visualización del modelo lineal
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Predicción líneal del sueldo en función del nivel de empleado") +
  xlab("Nivel del empleado") + 
  ylab("Sueld (en $)")
# Visualización del modelo polinomica
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Predicción polinomica del sueldo en función del nivel de empleado") +
  xlab("Nivel del empleado") + 
  ylab("Sueldo (en $)")


# Predicción de los nuevos resultados con la regresión lineal lineal

y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Predicción de los nuevos resultados con la regresión lineal polinomica

y_pred_poly = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5^2,
                                                Level3 = 6.5^3,
                                                Level4 = 6.5^4))


