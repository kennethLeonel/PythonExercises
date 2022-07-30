import numpy as np

#Primer punto
print("--------------- seccion numpy primer ejercicio -----------------")
arreglo1 = np.zeros(10)
print(arreglo1)
print("--------------- seccion numpy segundo ejercicio -----------------")
arreglo2 = np.ones(10)
print(arreglo2)

print("--------------- seccion numpy tercer ejercicio  Tile -----------------")
#Arreglo de diez 5 
arreglo3 = np.tile(5,12) # 12 veces el numero 5
arreglo3p1 = np.ones(12) * 5
arreglo3p2 = np.zeros(12) + 5
print(arreglo3)
print("--------------- seccion numpy cuarto ejercicio  -----------------")
arreglo4 = np.arange(10,51) # desde 10 hasta 50
print(arreglo4)
print("--------------- seccion numpy quinto ejercicio  -----------------")
arreglo5= np.arange(10,51,2) # desde 10 hasta 50 con incremento de 2
print(arreglo5)
print("--------------- seccion numpy sexto ejercicio  -----------------")

arreglo6 = np.array([[0,1,2],[3,4,5],[6,7,8]])
arreglo6p = np.arange(0,9).reshape(3,3)
print(arreglo6)
print("--------------- seccion numpy septimo ejercicio  -----------------")
# matriz de identidad
arreglo7 = np.identity(3)
print(arreglo7)
print("--------------- seccion numpy octavo ejercicio  -----------------")
#Numero aleatorio entre 0 y 1
numeroAle = np.random.rand(1)
print(numeroAle)
print("--------------- seccion numpy noveno ejercicio  -----------------")
arreglo9 = np.random.normal(0,2,25) # 25 numeros aleatorios con distribucion normal
arreglo9p = np.random.randn(25) # 25 numeros aleatorios con distribucion normal
print(arreglo9)
print("--------------- seccion numpy decimo ejercicio  -----------------")
arreglo10 = np.zeros(100).reshape(10,10) # 100 ceros
#Mejor la de abajo
arreglo10p =np.arange(0.01,1.01,0.01).reshape(10,10) # 100 cerosnumeros entre 0 y 1 con incremento de 0.01
print(arreglo10p)
print("--------------- seccion numpy onceavo ejercicio  -----------------")
arreglo11 = np.linspace(0,1,20).reshape(4,5) # 20 numeros entre 0 y 1 con incremento de 0.25
print(arreglo11)
print("--------------- seccion numpy ejercicio  indexing -----------------")
arregloIndexing =np.arange(1,26).reshape(5,5) # 5x5 con numeros del 1 al 25
print(arregloIndexing)
#Punto 12
print("............................. Punto 12 .............................")
arreglo12 =arregloIndexing[2:,1:]
print(arreglo12)
#Punto 13

print("............................. Punto 13 .............................")
arreglo13 =arregloIndexing[3:4,4:5]
arreglo13p = arregloIndexing[3,4]
print(arreglo13p)
print("...")
print(arreglo13)
#Punto 14
print("............................. Punto 14 .............................")
arreglo14 =arregloIndexing[:3,1:2]
print(arreglo14)
#Punto 15
print("............................. Punto 15 .............................")

arreglo15 =arregloIndexing[4:5]
print(arreglo15)
#Punto 16
print("............................. Punto 16 .............................")
arreglo16 =arregloIndexing[3:5]
print(arreglo16)
#Punto 17
print("............................. Punto 17 .............................")
suma = arregloIndexing.sum()
print(suma)
#Punto 18
print("............................. Punto 18 .............................")
desviacion = arregloIndexing.std()
print(desviacion)
#Punto 19
print("............................. Punto 19 .............................")
sumaPorColumna = arregloIndexing.sum(axis=0)
print(sumaPorColumna)


