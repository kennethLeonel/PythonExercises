#########Librerias##############  
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

#################################
print("-------Sección Matrix plots--------")


print("-------Datos tips--------")
datosTips = sns.load_dataset('tips') # Es un dataset que ya tiene la librería 
print(datosTips.head())

print("-------Datos flights--------")
datosFligts = sns.load_dataset('flights')
print(datosFligts.head())

#Para que un mapa de calor funcione correctamente se necesita que los datos esten en forma de matriz
# y a su vez que tanto como las filas y columnas tengan el mismo nombre o indice ( practicamente tener una matriz de correlación)
# Sirve sobre todo para ver comprender la relaciones entre variables que ayuden a identificar los datos para hacer un modelo predictivo

print("-------Datos tips.corr()--------")

correlacionTips = datosTips.corr()
print(correlacionTips) # se muestra la matriz de correlación de los datos tips

sns.heatmap(correlacionTips, annot=True, cmap='coolwarm') # se muestra el mapa de calor de los datos tips
plt.show()

# sns.clustermap(correlacionTips, cmap='coolwarm') # se muestra el mapa de calor de los datos tips con cluster

print("-------Datos flights.pivot_table()--------")
## es mejor dejar como values la variable que sea numerica	
correlacionFlights = datosFligts.pivot_table(values='passengers', index='month', columns='year') # se crea una matriz de correlación con los datos flights
print(correlacionFlights)
sns.heatmap(correlacionFlights, cmap ='magma', linecolor = 'white', linewidths=1) # se muestra el mapa de calor de los datos flights
plt.show()
sns.clustermap(correlacionFlights, cmap ='coolwarm', standard_scale=1) # se muestra el mapa de calor de los datos flights con cluster, el parametro de standard_Scale permite en normalzar los datos entre 0 y 1
plt.show()


