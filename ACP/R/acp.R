# análisis de componentes principales

# importar el dataset
dataset = read.csv('Wine.csv')

# Dividir el dataset en el conjunto de entrenamiento y en el conjunto de testing
library(caTools)
set.seed(123)
split = sample.split(dataset$Customer_Segment, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Escalado de las variables
training_set[,-14] = scale(training_set[,-14])
testing_set[,-14] = scale(testing_set[,-14])

# Proyección de los componentes principales
library(caret)
library(e1071)

pca = preProcess(x=training_set[,-14], method = "pca", pcaComp = 2)
training_set = predict(pca, training_set)
training_set = training_set[,c(2,3,1)]

testing_set = predict(pca, testing_set)
testing_set = testing_set[,c(2,3,1)]

# Ajustar el modelo de regresión logística con el conjunto de entrenamiento
classifier = svm(formula = Customer_Segment ~ .,
                 data = training_set,
                 type = "C-classification",
                 kernel = "linear")


# Predicción de los resultados con el conjunto de testing
y_pred = predict(classifier, newdata = testing_set[,-3])

# Crear la matriz de confusiones
cm = table(testing_set[,3], y_pred)

# Visualización del conjunto de entrenamiento
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))