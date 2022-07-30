
from random import Random
from tkinter import OUTSIDE
import pandas as pd
import numpy as np

# para utilizar los datframes importamos lo siguiente
from numpy.random import randn

print ("--------------- seccion pandas primer ejercicio  -----------------")
# manipular la series con pandas

etiquetas = ['A','B','C','D','E']
numeros = [10,20,30,40,50]
serie1 = pd.Series(data =numeros,index=etiquetas) # aca modificamos el index
print(serie1)
# para acceder a un valor de la serie usamos el index que en este caso son las etiquetas
print("valor de la serie usamos el index que en este caso son las etiquetas serie1['A'] es igual a:" ,serie1['A'])

print("--------------- seccion pandas segundo ejercicio  -----------------")
# manipular la series con pandas utilizando diccionarios
diccionario = {'A':10,'B':20,'C':30,'D':40,'E':50}
series2= pd.Series(data=diccionario)
print(series2)
print("--------------- seccion pandas tercer ejercicio error data -----------------")
series3 = pd.Series(data=diccionario,index=['A','B','C','D','j'])
print(series3)

print("--------------- seccion pandas cuarto ejercicio  -----------------")
serie4_1 = pd.Series(data = [1,2,3,4,5] , index=['Colombia','Argentina','Brasil','Chile','Uruguay'])
print(serie1)
serie4_2 = pd.Series(data = [1,2,8,5,9],index = ['Colombia','Argentina','Brasil','Chiles','Uruguays'])
print(serie4_2)

print("--------------- Sumando series pandas del cuarto ejercicio -----------------")
print(serie4_1 + serie4_2)
print("--------------- observamos que tiene valores NaN lo que es chile, chiles, uruguay y uruguays ya que no es el mismo index -----------------")



print("--------------- Sección de dataframes -----------------")
# crear un dataframe 
# definimos la semilla 
seed = np.random.seed(101) # 101 es la semilla
df = pd.DataFrame(data = np.array([0, -1, 3, 4, 5, -5, -12, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape(5,4), index= ['A','X','C','D','E'], columns=['col1','col2','col3','col4']) 
print(df)
print("Coger serie de la col1: ", df['col1']) # el DataFrame es un conjunto de series de pandas
print("Coger serie de la col2: con index  D :", df['col2']['D'])
print("Coger serie de la col3: con otro méto no recomendable para manipular los dataframes  ", df.col3.D)
print("Coger serie de la col4, col1 para ello es coger una lista de series de pandas", df[['col4', 'col1']])

print("..........")
df['columnaNueva'] = df['col1'] + df['col1']
print(df)
print ("\n=================Eliminar columna======================")
df.drop('columnaNueva', axis=1, inplace=True) # se debe colocar el nombre de la columna que queremos eliminar junto con axis =1 y para confirmar que queremos elimanrlo de dataframe inplace=True
print(df)
print ("\n=================Eliminar fila======================")
df.drop('A', axis=0, inplace=True) # se debe colocar el nombre de la fila que queremos eliminar junto con axis =0 y para confirmar que queremos elimanrlo de dataframe inplace=True
print(df)
# coger el index D :", df[['col2', 'col3']]['D'])
print("\n=================Coger una fila======================")
print("\nCoger serie de la col2 y col3: ", df[['col2', 'col3'][1]])

print("\n=====================Ejercicio loc ====================")
print("\nCoger serie de la col2 y col3: ", df.loc['X', ['col2', 'col3']]) # se toma el index de la fila y se toma el index de la columna que queremos tomar
print ("\n=====================Ejercicio iloc ====================")
print("\nCoger serie de la col2 y col3: ", df.iloc[0, [1, 2]]) # se toma el index de la fila y se toma el index de la columna que queremos tomar
print("Probar", df.loc[['X','D'], ['col2', 'col3']])

mayor_a_cero = df > 0
print(mayor_a_cero)
print(df[mayor_a_cero]) # los valores qeu estan en false aparecen como NaN
print("Mostrar solo los valores mayores a cero: ", df[df['col2'] < 0]) #solo mostrara la filas que contiene la columna 2 menores a 0
print(df)
print ("Mostrar solo dos columnas 3 y 4 donde la columna 2 sea < 0 \n", df[df['col2']<0][['col3', 'col4']])
print ("Mostrar solo dos columnas 3 y 4 donde la columna 2 sea < 0 \n", df[df['col2']>0][['col3', 'col4']])
print ("utilizar condiciones: and \n", df[(df['col2']<0) & (df['col3']<0)])
print ("utilizar condiciones: or y solo tomar los valores de la col1 \n", df[(df['col2']>0) | (df['col3']<0)]['col1'])

print ("\n=====================Ejercicio función reset_index() ====================")
nuevoDf = df.reset_index() # inplace=True para que se cambie la información
print("\nmirar que hace la función \n", nuevoDf) 
print(nuevoDf)
print("-------------------------------")
print(nuevoDf['col1'][0]) # el valor de la columna 1 en la fila A es 0
#print(df['col1']['B']) # el valor de la columna 1 en la fila B es PERO YA NO EXISTE ESE INDEX

print("=====================Ejercicio función set_index() ====================")
palabras =("Colombia,Argentina,Brasil,Chile").split(',')
print (palabras) # arreglo 
df['nuevoIndex']= palabras
print(df)
print("---- cambiando index")
print(df.set_index('nuevoIndex')) # cambia el index de la serie por el nuevo index 

print("\n=====================Ejercicio función sort_index() ====================")
print(df.sort_index()) # ordena el index 



print ("\n=====================Como manipular los frames nuevoDf====================")

nuevoDf= df['col2'] >0
print(df[nuevoDf]) # muestra solo las filas que cumplen la condicion
print("solo muestra la columna que deseo de ese nuevodf", df[nuevoDf]['nuevoIndex'].C)# muestra solo la columna que deseo de ese nuevodf y que sea el index C que contiene el valor de Argentina
print("solo muestra la columna que deseo de ese nuevodf", df[nuevoDf][['nuevoIndex', 'col4']]) 
print("solo muestra la columna que deseo de ese nuevodf", df[nuevoDf][['nuevoIndex', 'col4'][0]])
print("MUESTRA EL CONTENIDO DE LA FILA C que cumpla con el nuevodf \n", df[nuevoDf].loc['C',['nuevoIndex', 'col4']]) 
print("MUESTRA EL CONTENIDO DE LA FILA C que cumpla con el nuevodf \n", df[nuevoDf].loc['C',['nuevoIndex', 'col4'][0]]) # TENER EL VALOR

print("\n=====================Sección multiindex ====================")

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside)) # crea una lista donde cada index contiene una tupla
print("primera tupla \n", hier_index[0]) # MUESTRA LA TUPLA EN LA POSICIÓN 0
otroIndex = hier_index
otroIndex = pd.MultiIndex.from_tuples(otroIndex)
print ("se muestra multiIndex \n",otroIndex)
print("pasos para armar el multiIndex")
df2 = pd.DataFrame(randn(6,2), otroIndex, ['seccion1', 'seccion2'])
print(df2)
print("\n=====================Sección multiindex accediendo con Loc ====================")
print ("Accediendo al index G1 que contiene 3 filas \n",df2.loc['G1']) # muestra la fila G1 que contiene 3 filas
print ("Accediendo al index G1 que contiene 3 filas solo de la sección 1\n",df2.loc['G1']['seccion1']) # muestra la fila G1 que contiene 3 filas
print ("Accediendo al index G1 solo de la sección 2 que este en la fila 1\n",df2.loc['G1'].loc[1]['seccion2']) # muestra la fila G1 que contiene 3 filas
print ("Accediendo al index G1 solo de la sección 2 que este en la fila 1 y 2\n",df2.loc['G1'].loc[[1,2]]['seccion2']) # muestra la fila G1 que contiene 3 filas

print("\n=====================Sección multiindex agregarles nombreIndex  ====================")
df2.index.names = ['grupo', 'numero']
print("Agregando names al index pero no se manipulan\n\n",df2)
print("\n=====================Sección multiindex funcion xs tranversal ====================")
print("\nmostrar solo los valores 1 del dataframe", df2.xs(1,level ='numero')) # muestra solo los valores 1 del dataframe
print("Mostrar grupo G1 y numero 1 del dataframe\n", df2.xs(('G1',1),level =['grupo','numero'])) # muestra solo los valores 1 del dataframe

print ("==========Sección Missing Data==================")
diccionarioMissingData = {
    'A': [
        1,
        2,
        np.nan
    ],
    'B': [
        5,
        np.nan,
        np.nan
    ],
    'C': [
        1,
        2,
        4
    ]
}
dfMissingData = pd.DataFrame(diccionarioMissingData)
print(dfMissingData)

print("\n=====================Sección Missing Data dropna()==================")

print ("Eliminar filas que contengan datos NaN \n",dfMissingData.dropna()) # elimina las filas que contengan datos NaN
print ("Eliminar columnas que contengan datos Nan\n", dfMissingData.dropna(axis= 1))#Recuerda axis = 1 es columnas axis = 0 es filas
print ("Eliminar filas que contengan al menos dos datos Numericos  \n",dfMissingData.dropna(thresh=2)) # elimina las filas que contengan datos NaN

print ("\n ======================Sección Missing Data fillna()==================")
print ("Reemplazar datos NaN con valor por datos perdido \n",dfMissingData.fillna(value ='DATO PERDIDO')) # reemplaza los datos NaN con el valor dATO PERDIDO
print ("Reemplazar datos NaN solo de la columna A con valor promedio de la columna A \n",dfMissingData['A'].fillna(value=dfMissingData['A'].mean())) # reemplaza los datos NaN con el valor promedio de la columna
print ("Reemplazar datos NaN con valor promedio de la columna A \n",dfMissingData.fillna(value=dfMissingData['A'].mean())) # reemplaza los datos NaN con el valor promedio de la columna


print ("==========Sección GROUPBY==================")

dataGroupBy = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
dfGroupBy = pd.DataFrame(dataGroupBy)
print(dfGroupBy)
print("\n=====================Sección GROUPBY groupby()==================")
objetoDFGroup = dfGroupBy.groupby('Company')
print("\nAgrupamos por Company\n",objetoDFGroup) # agrupa por Company
print("\nAgrupamos por Company y obtenemos el promedio\n",objetoDFGroup.mean()) # agrupa por Company y obtenemos el promedio se ignora los valores que no sean numericos
print("\nAgrupamos por Company y obtenemos la suma que hizo la compañia GOOG\n",objetoDFGroup.sum().loc['GOOG'].Sales) # agrupa por Company y obtenemos el promedio se ignora los valores que no sean numericos
print("\nAgrupamos por Company y obtenemos la cantidad de datos por empresa\n",objetoDFGroup.count()) 
print("\nAgrupamos por Company y obtenemos el dato minimo por empresa\n",objetoDFGroup.min()) # agrupa por Company y obtenemos el dato minimo por empresa
print("\nAgrupamos por Company y obtenemos el dato maximo por empresa\n",objetoDFGroup.max()) # agrupa por Company y obtenemos el dato maximo por empresa
print("\nAgrupamos por Company y obtenemos datos significatiuvos de la empresa\n",objetoDFGroup.describe()) # agrupa por Company y obtenemos datos significatiuvos de la empresa 
print("\nAgrupamos por Company y obtenemos datos significatiuvos de la empresa\n",objetoDFGroup.describe().transpose()) # agrupa por Company y obtenemos datos significatiuvos de la empresa

print("\n=====================Sección Merging Joining and concatening==================")

dfMerge = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                          index=[0, 1, 2, 3])
dfMerge2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                            index=[4, 5, 6, 7])
dfMerge3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                            index=[8, 9, 10, 11])

print("==========Sección concatenation==================")
print("\nConcatenamos dos dataframes\n",pd.concat([dfMerge,dfMerge2])) # concatena dos dataframes
print("\nConcatenamos tres dataframes mediante columnas\n",pd.concat([dfMerge,dfMerge2,dfMerge3], axis=1)) # concatena dos tres dataframes es malo con columnas

dfMerge4 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3'],
                         'Key': ['K0', 'K1', 'K2', 'K3']},
                            index=[0, 1, 2, 3])
dfMerge5 =pd.DataFrame({  'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3'],
                          'Key': ['K0', 'K1', 'K2', 'K3']}, 
                            index=[0, 1, 2, 3])
print("==========Sección merging==================")
print("\nMergeamos dos dataframes\n",pd.merge(dfMerge4,dfMerge5,how='inner',on='Key')) # mergeamos dos dataframes
 


dici ={'A': ['A0', 'A1', 'A2'],'B': ['B0', 'B1', 'B2']}
print("\nDiccionario\n",dici)
dfDic = pd.DataFrame(dici , index=['K0', 'K1', 'K2'])
print("\nDiccionario\n",dfDic)
dici2 ={'C': ['C0', 'C2', 'C3'],'D': ['D0', 'D2', 'D3']}
print("\nDiccionario\n",dici2)
dfDic2 = pd.DataFrame(dici2 , index=['K0', 'K2', 'K3'])
print("\nDiccionario\n",dfDic2)
print("Utilizar Join \n", dfDic.join(dfDic2)) # join  donde prevalece dfDic en este caso no se cruza con la k3
print("Utilizar Join Outer \n", dfDic.join(dfDic2, how='outer')) # join  donde prevalece dfDic en este caso no se cruza con la k3
print ("Utilizar Join Left \n", dfDic.join(dfDic2, how='left')) # join  donde prevalece dfDic en este caso no se cruza con la k3
print ("Utilizar Join right \n", dfDic.join(dfDic2, how='right')) # join  donde prevalece dfDic en este caso no se cruza con la k3
print ("Utilizar Join inner \n", dfDic.join(dfDic2, how='inner')) # join  donde prevalece dfDic en este caso no se cruza con la k3
print ("Utilizar Join dfDic2 \n", dfDic2.join(dfDic)) # join  donde prevalece dfDic2 en este caso no se cruza con la k1

print("==================Seccion operaciones==================")
dicto = {
    'Col1': [1, 2, 3, 4],
    'Col2': [40, 20, 30, 40],
    'Col3': ['abc', 'def', 'ghi', 'jkl']
}
dfo = pd.DataFrame(dicto)
print("\nDataframe\n",dfo.head())

print("\nDataframe tomar columna2\n",dfo['Col2'].unique())
print("\nDataframe tomar columna2 contador de valores\n",dfo['Col2'].value_counts())
print("\nDataframe tomar columna2 contador de valores organizado menor a mayor\n",dfo['Col2'].value_counts().sort_index())
print("\nDataframe tomar columna2 cantidad de valores len \n",len(dfo['Col2'].unique()))
print("\nDataframe tomar columna2 cantidad de valores nunique\n",dfo['Col2'].nunique())

def my_function(x):
    return x*2

print("\nDataframe tomar columna2 contador de valores funcion\n",dfo['Col2'].apply(my_function))
print("\nDataframe tomar columna 2 y aplicar len\n",dfo['Col3'].apply(len)) # aplicar len a la columna 3 solo valores string}
print("\nDataframe tomar columna 2 y aplicar lambda\n",dfo['Col2'].apply(lambda x: x *2)) # aplicar len a la columna 3 solo valores string}

print("valores null\n",dfo.isnull())

print("==================Seccion input and Output==================")

archivoSalida = dfo.to_csv('salida.csv', index=False) # Es mejor asi para que no agregue un index adicional
archivoLeer = pd.read_csv('salida.csv')
print("Archivo leido\n",archivoLeer)
print ("Excel.... falla")
# archivoSalidaExcel = df.to_excel('salida2.xlsx', sheet_name='salida') # Es mejor asi para que no agregue un index adicional
# archivoLeerExcel = pd.read_excel('salida2.xlsx', sheet_name='salida')

print("==================leeer html==================")
#datosHtml = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
#datoshtml2= pd.read_html('https://en.wikipedia.org/wiki/Minnesota')

#print("\nDataframe leer html\n",len(datosHtml2))




