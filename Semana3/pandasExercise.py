


import pandas as pd

pd.options.display.max_columns = 13 #para mostrar todas las columnas
pd.options.display.max_rows = None #para mostrar todas las filas
archivoSaliries = pd.read_csv('salaries.csv')
print("Leyendo archivo \n",archivoSaliries.head())

print("\n Informacion archivo \n",archivoSaliries.describe())
print("\n Informacion archivo2 \n",archivoSaliries.info())
print("\n Informacion promedio BasePay \n",archivoSaliries['BasePay'].mean())

datosBasePay = archivoSaliries.loc[:,'BasePay']
#datosBasePay.drop(values='NOT PROVIDED', inplace=True)
# filtro = datosBasePay.isin(['NOT PROVIDED'])
# datosBasePay = datosBasePay[~filtro]
# print("\n BasePay sin NOT PROVIDED \n",datosBasePay.head())
datosBasePay = datosBasePay.replace('NaN', 'Not Provided')
filtro = datosBasePay != 'Not Provided'                                                                             
print("\n BasePay sin NOT PROVIDED promedio \n",datosBasePay[filtro].mean())

print("\n Datos BasePay describe \n",datosBasePay.describe())
print("\n El dato mas alto es \n",archivoSaliries['OvertimePay'].max())

filtro2 = (archivoSaliries['EmployeeName'] == 'JOSEPH DRISCOLL') | (archivoSaliries['EmployeeName'] == 'Joseph Driscoll')
print("\n JOSEPH DRISCOLL trabajo \n",archivoSaliries[filtro2].JobTitle)
print("\n JOSEPH DRISCOLL trabajo2 \n",archivoSaliries[filtro2]['JobTitle'])

print ("\n JOSEPH DRISCOLL ganancias \n",archivoSaliries[filtro2]['TotalPayBenefits'])

filtro3 = archivoSaliries['TotalPayBenefits'].idxmax()
print("\n Mejor empleado ganancias max \n",archivoSaliries.loc[filtro3])

filtro4 = archivoSaliries['TotalPayBenefits'].max() == archivoSaliries['TotalPayBenefits']
print("\n Mejor empleado ganancias max solo nombre  \n",archivoSaliries[filtro4]['EmployeeName'])

filtro5 = archivoSaliries['TotalPayBenefits'].idxmin()
print("\n Peor empleado ganancias min \n",archivoSaliries.loc[filtro5].EmployeeName)
filtro6 = archivoSaliries['TotalPayBenefits'].min() == archivoSaliries['TotalPayBenefits']
print("\n Peor empleado ganancias min solo nombre \n",archivoSaliries[filtro6])

filtro7 = archivoSaliries['Year'] > 2010
agrupar = archivoSaliries[filtro7].groupby('Year')
print("\n Agrupacion por año \n", agrupar['BasePay'].mean())
filtro8=  archivoSaliries['BasePay'].mean()
print("\n Promedio BasePay desde el 2011 \n",archivoSaliries[filtro7]['BasePay'].mean())

print("\n cantidad de trabajos unicos \n",archivoSaliries['JobTitle'].nunique())
print("\n Agrupacion por JobTitle \n",archivoSaliries['JobTitle'].value_counts().head(5))
print("===================Revisar=====================")
hey = sum(archivoSaliries[archivoSaliries['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...
print("\n cantidad de trabajos unicos en el año 2013 \n",hey)

def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
hey2 =sum(archivoSaliries['JobTitle'].apply(lambda x: chief_string(x)))
print("\n cantidad de trabajos unicos en el año 2013 \n",hey2)

archivoSaliries['title_len'] = archivoSaliries['JobTitle'].apply(len)
print("\n Correlacion \n",archivoSaliries[['title_len','TotalPayBenefits']].corr())

#--------Ecommerce ejercicio-----------------------------

archivoEcomerce = pd.read_csv('ecommerce.csv')
print("\n Leyendo archivo ecomerce \n",archivoEcomerce.head())
print ("Informacion")

print(archivoEcomerce.info())

promedio = archivoEcomerce['Purchase Price'].mean()
print("\n Promedio de compra \n",promedio)
Alto = archivoEcomerce['Purchase Price'].max()
print("\n Maximo de compra \n",Alto)
Bajo = archivoEcomerce['Purchase Price'].min()
print("\n Minimo de compra \n",Bajo)

contador = archivoEcomerce[archivoEcomerce['Language']== 'en'].count()
print("\n Cantidad de registros en ingles \n",contador)

lawyer = archivoEcomerce[archivoEcomerce['Job']== "Lawyer"].count()
print("\n Cantidad de registros en Lawyer \n",lawyer)

lawyer2 = len(archivoEcomerce[archivoEcomerce['Job']== "Lawyer"].index)
print("\n Cantidad de registros en Lawyer mediante función len() \n",lawyer2)

compradoresAM =archivoEcomerce[archivoEcomerce['AM or PM']== 'AM'].value_counts().count()
print("\n Cantidad de compradores AM \n",compradoresAM)

compradoresPM =archivoEcomerce[archivoEcomerce['AM or PM']== 'PM'].value_counts().count()
print("\n Cantidad de compradores PM \n",compradoresPM)

mejores = archivoEcomerce['Job'].value_counts().head(5)
print("\n Mejores trabajos \n",mejores)

lote = archivoEcomerce[archivoEcomerce['Lot'] == '90 WT']
print("\n Lote 90 WT \n",lote['Purchase Price'])

tarjeta = archivoEcomerce[archivoEcomerce['Credit Card'] == 4926535242672853]
print("Dueño", tarjeta['Email'])

americanCard = archivoEcomerce[(archivoEcomerce['CC Provider'] == 'American Express') & (archivoEcomerce['Purchase Price'] > 95 )]
print("\n American Express \n",americanCard.count())

def los_Que_Expiran(expiracion):
    contenido = expiracion.split('/')
    if contenido[1] == '25':
        return True
    else:
        return False

expiran = sum (archivoEcomerce['CC Exp Date'].apply(lambda x: los_Que_Expiran(x)))
print("\n Cantidad de tarjetas que expiran en el 2025 \n",expiran)

hosts = archivoEcomerce['Email'].str.split('@').str[1]
contadorHost =hosts.value_counts().head(5)
print("\n Cantidad de hosts \n",contadorHost)