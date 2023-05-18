import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cargamos el dataset de seaborn llamado iris

dataIris = sns.load_dataset('iris')

print ("----data Iris----- ")

print (dataIris.head())

print ("----data Iris solo detallar las unicas especies----- ")
arregloEspecies = dataIris['species'].unique()
print (arregloEspecies)

print("--- hacer pairplot-----")
sns.pairplot(dataIris)
plt.show()

print("--- hacer un grid template-----")
grid = sns.PairGrid(dataIris)
grid.map_upper(plt.scatter)
grid.map_lower(sns.kdeplot, cmap = "Blues_d")
grid.map_diag(sns.kdeplot, lw = 3, legend = False)

plt.show()