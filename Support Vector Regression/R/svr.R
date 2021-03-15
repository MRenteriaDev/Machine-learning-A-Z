#Support Vector Regression

#Import the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

#Adjust SVR with dataset
install.packages("e1071")
library(e1071)

# build a SVR object
regression = svm(formula = Salary ~ .,
                 data = dataset,
                 type = "eps-regression",
                 kernel = "radial")

#Predict the new results with the SVR
y_pred = predict(regression, newdata = data.frame(Level = 6.5))

#See the SVR Model
library(ggplot2)

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x= dataset$Level, y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Prediction (SVR)") +
  xlab("Employed Level") +
  ylab("Salary Estimed ($USD)")
# Ignorar sueldo de CEO por valor atipico
            