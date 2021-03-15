# Apriori

datatset = read.csv('./Market_Basket_Optimisation.csv', header = FALSE)
datatset = read.transactions('Market_Basket_Optimisation.csv', sep = ",",
                             rm.duplicates = TRUE)
summary(datatset)

itemFrequencyPlot(datatset, topN=10)

# Entrenar el algoritmo a apriori con el dataset
rules = apriori(data = datatset, 
                parameter = list(support= 0.003, confidence =0.4))

# Visualización de los resultados
inspect(sort(rules, by = 'lift')[1:10])
