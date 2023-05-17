
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips") # se carga un dataset que tiene por defecto 
print (tips.head())
#Mirar comportamiento de total_bill

sns.distplot(tips['total_bill'], kde=True, bins=40)# se muestra el comportamiento de total_bill / muestra grafico sobre la estimación de desnsidad kernel
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')# se muestra  grafica con regresion, el tipo si se quiere se puede dejar vacio o hex o kde
plt.show()

sns.pairplot(tips, hue='sex', palette='coolwarm')# se muestra grafico de dos dimensiones con el color de los datos depedniendo de una varaible categorica
plt.show()

sns.rugplot(tips['total_bill']) # muestra una distribución de los puntos deshonesta, mediante esa forma se hace la estimacion de la desnsidad de kernel
plt.show()

sns.kdeplot(tips['total_bill'], shade=True)# Se hace la estimacion de la desnsidad de kernel
plt.show()

print("--GRÁFICAR VARIABLES CATEGORICAS--")

sns.barplot(x='sex',y='total_bill', data = tips, estimator = np.std) 
plt.show()

sns.countplot(x='sex',  data = tips)# se muestra el conteo de la variable categorico sex ocurrencias de cada tipo de sexo
plt.show()

sns.boxplot(x='sex', y='total_bill', data = tips)
plt.show()

# se puede modificar los parametros del boxplot para poder compararlo junto con otra variable categorica se coloca el hue
sns.boxplot(x='sex', y='total_bill', data = tips, hue='smoker')
plt.show()

#existe un plot super raro llamado violinplot que se puede considerar
# igual que la de boxplot pero violinplot brinda más información y permite hacer otras cosas con sus parametros permitidos
sns.violinplot(x='sex', y='total_bill', data = tips) # sencilla
plt.show()

#forma normal con el hue
sns.violinplot(x='sex', y='total_bill', data = tips, hue='smoker')
plt.show()

#forma interesante para comarar las dos variables categoricas de manera mas simplificada que junta la distribución de densidad de la variables categoricas 
sns.violinplot(x='sex', y='total_bill', data = tips, hue='smoker', split=True)
plt.show()

#striplot x variable categorica , y variable numerica simple

sns.stripplot(x='sex', y='total_bill', data = tips, hue='smoker', jitter=True)# El jitter es para que muestre los puntos del ataset no apeñuscados
plt.show()

#Este gráfico funciona mejor para dataset pequeños
sns.violinplot(x='day',y='total_bill',data=tips) # en el violinplot agregamos la parte de los swarmplot
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
plt.show()

#factorPlot, sepuede crear cualquier tipo de grafico que se ha tomado, mediante el parametro kind
sns.catplot(x='day',y='total_bill',data=tips, kind='bar') 
plt.show()


print("-------Sección Matrix plots--------")

datosTips = sns.load_dataset('tips') # Es un dataset que ya tiene la librería 
print(datosTips.head())



