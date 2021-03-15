# Algorithm de la regression lineal simple


# import data
dataset = read.csv('./Salary_Data.csv')

# Dividir los datos en un conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# ajustar el modelo de regresión lineal simple con el conjunto de entrenamiento
# la tilde marca el "en función de"
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

# Predecir los resultados con el conjunto de test
y_pred = predict(regressor, newdata = testing_set)

# Visualización de los resultados del conjunto del entrenamiento
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de entrenamiento)") +
  xlab("Años de Experiencia") + 
  ylab("Sueldo (en $)")

#Visualización de los resultados en el conjunto de testing
ggplot() +
  geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary),
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Testing)") +
  xlab("Años de Experiencia") + 
  ylab("Sueldo (en $)")