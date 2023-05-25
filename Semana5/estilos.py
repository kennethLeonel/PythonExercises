import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

print("Se empieza con los estilos de Seaborn")
#Se va utiliar la función countplot para poder graficar y deben ser con variaboles categoricas
# Se carga dataset de tips desde seaborn 
dataTips = sns.load_dataset('tips')
print (dataTips.head())
#Se configura el estilo el background del plot
sns.set_style('ticks') #Este puede ser none, white, whitegrid, ticks, darkgrid
sns.countplot(x='sex', data = dataTips)
#Quitar los ticks derecha con la función, se úede decir por parametros a que parte quitar lo que sería las lineas de referencia si es top, bottom, left, rigth
sns.despine( left=False, bottom=True)
plt.show()
#Ahora se va a utilizar lo que sería set_context para ajusatr la grafica según lo necesitemos
sns.set_context('poster', font_scale=3) #Puede ser ademas de poster, paper, notebook,talk,  por otro lado, el font scale es agrandarle dos veces apartir de ese contexto 
sns.countplot(x='sex', data = dataTips)
plt.show()

# Darle estilos de color a la gráfica con palette
sns.set_context('notebook') # Se ajusta de nuevo el contexto
sns.lmplot(x='total_bill', y='tip', data=dataTips, hue='sex', palette='cividis') #cividis, coolwarm
plt.show()
# Estos palletes se puede ver diferentes colores o temas buscandos matplotlib colormap https://matplotlib.org/stable/tutorials/colors/colormaps.html
