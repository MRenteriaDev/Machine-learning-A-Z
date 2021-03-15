# Clustering Jerárquico

dataset = read.csv('./Mall_Customers.csv')
X = dataset[,4:5]

# Utilizar el dendrograma para encontrar el número óptimo de clusters
dendrogram = hclust(dist(X, method = "euclidean"),
                    method = "ward.D")

plot(dendrogram,
     main = "Dendrograma",
     xlab = "lientes del centro comercial",
     ylab = "Distancia euclidiana" )


# Ajustar el clustering jerarquico al dataset
hc = hclust(dist(X, method = "euclidean"),
                    method = "ward.D")
y_hc = cutree(hc, k=5)

# Visualización de los clusters
library(cluster)

clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = "Clustering de clientes",
         xlab = "Ingresos anuales",
         ylab = "Puntuación de gastos")
