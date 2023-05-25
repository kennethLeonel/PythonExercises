import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt


print("Empieza Regression plots")


# Se carga dataset de tips desde seaborn 
dataTips = sns.load_dataset('tips')
print (dataTips.head())
# se va a crear L-M plot para hacer un trama lineas, donde tanto el eje x como y deben ser númericos 
sns.lmplot(x='total_bill', y='tip', data=dataTips)

#Si se desea mejor tener la regresion lineal teniendo en cuenta valores categoricos (sexo, cargos, o en e4ste caso time) se agrega el parametro hue
sns.lmplot(x='total_bill', y='tip', data=dataTips, hue='sex', markers=['o','v'])
# con time, pero se agregara lo que son scatter_kwas para poder tener una mejor escala del plot se ve más grandes als bolitas
sns.lmplot(x='total_bill', y='tip', data=dataTips, hue='time', scatter_kws={'s':100})

#dividir las regresiones en diferentes plots como en este caso con el paramtro col
sns.lmplot(x='total_bill', y='tip', data=dataTips, col='sex' )
#Si queremos que se pueda tener en cuenta otra variable categorica se hace de la sigueinte forma
sns.lmplot(x='total_bill', y='tip', data=dataTips, col='sex', row='time' )

sns.lmplot(x='total_bill', y='tip', data=dataTips, col='sex', row='time' , hue='smoker')
sns.lmplot(x='total_bill', y='tip', data=dataTips, col='day', hue='sex')
plt.show()