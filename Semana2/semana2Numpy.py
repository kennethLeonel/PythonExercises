import numpy as np

print("--------------- seccion numpy array -----------------")
## Crear un array
arreglo = np.array([1,2,3,4,5])
print(arreglo)
print(arreglo.shape)

print("--------------- seccion numpy matriz 3x3 array -----------------")
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
## dimension de la matriz
print(matriz.shape)

print("--------------- seccion numpy random -----------------")
## Crear un array de numeros aleatorios
arregloRandom = np.random.rand(10) # 10 numeros aleatorios entre 0 y 1
print(arregloRandom)

arregloRandom2 = np.random.rand(10,10) # 10x10 numeros aleatorios entre 0 y 1
print(arregloRandom2)

print("--------------- seccion numpy random randint -----------------")
arregloRandom3 = np.random.randint(0,10,(3,3)) # 3x3 numeros aleatorios entre 0 y 10 
print(arregloRandom3)

print("--------------- seccion numpy arange -----------------")
arregloRandom4 = np.arange(0,12,2) # 0,2,4,6,8,10 -> 12 es el limite sin incluir y 2 es el incremento
print(arregloRandom4)

print("--------------- seccion numpy zeros -----------------")
arregloRandom5 = np.zeros((3,3)) # 3x3 array de ceros
print(arregloRandom5)

print("--------------- seccion numpy ones -----------------")
arregloRandom6 = np.ones((3,3)) # 3x3 array de unos
print(arregloRandom6)

print("--------------- seccion numpy eye -----------------")
arregloRandom7 = np.eye(3) # 3x3 array de unos en la diagonal
print(arregloRandom7)

print ("--------------- seccion numpy identity -----------------")
arregloRandom8 = np.identity(3) # 3x3 array de unos en la diagonal
print(arregloRandom8)

print("--------------- seccion numpy random uniform -----------------")
arregloRandom9 = np.random.uniform(0,10,(3,3)) # 3x3 array de numeros aleatorios entre 0 y 10
print(arregloRandom9)

print("--------------- seccion numpy random normal -----------------")
arregloRandom10 = np.random.normal(0,10,(3,3)) # 3x3 array de numeros aleatorios con distribucion normal
print(arregloRandom10)

print("--------------- seccion numpy random permutation -----------------")
arregloRandom11 = np.random.permutation(10) # 10 numeros aleatorios entre 0 y 9
print(arregloRandom11)

print("--------------- seccion numpy linspace -----------------")
arreglo12 = np.linspace(0,10,10) # 10 numeros  entre 0 y 10 donde el inicio es 0 y el final es 10 y el numero de elementos es 10
print(arreglo12)

print("--------------- seccion numpy linspace2 -----------------")
m = np.linspace(10, 40, 4)
print(m)

print("--------------- seccion numpy logspace -----------------")
m2 = np.logspace(2, 3, 10)
print(m2)
print("--------------- seccion numpy logspace explicación -----------------")
## para comprender logspace es lo siguiente
# coge la funcion linspace 
resultado = np.linspace(2, 3, 10)
print(resultado)
# y le aplica la funcion pow para elevar el valor de cada elemento del array resultado 
resultado2 = np.power(10, resultado) # 10 es el exponente y resultado es el array de numeros -> 10^2, 10^2.111111 etc
print(resultado2)

print("--------------- seccion numpy reshape -----------------")
arregloNormal = np.array([1,2,3,4,5,6,7,8,9,10])

print("Arreglo normal: ", arregloNormal)
print("Arreglo normal reshape:2x5 ", arregloNormal.reshape(2,5))# 2x5
print("Arreglo normal reshape:5x2 ", arregloNormal.reshape(5,2))# 5x2
print("numero maximo: ", np.max(arregloNormal))
print("numero minimo: ", np.min(arregloNormal))
print("posicion del numero maximo: ", np.argmax(arregloNormal))
print("posicion del numero minimo: ", np.argmin(arregloNormal))
print("tipo de dato: ", arregloNormal.dtype)

numeroAleatorio = np.random.randint(4,8)  # numero aleatorio entre 4 y 8
print("numero aleatorio: ", numeroAleatorio)



# print("--------------- seccion Sarah-----------------")
# arreglosarah= ["Desayuno","Almuerzo","Cena", "Baño", "Cocina", "ceppilo"] 
# print(arreglosarah)

# #Recoorrer actividades arregloSarah
# for actividad in arreglosarah:
#     if actividad != "jugar":
#         print("jugar No esta en el arreglo")
#     if actividad == "ceppilo":
#         print("jugar Se agregara al arreglo")
#         arreglosarah.append("jugar")    
# print(arreglosarah)

print("--------------- seccion Numpy Indexing-----------------")
arregloIndex = np.arange(0,11)
print(arregloIndex)
print(arregloIndex[0:3]) # 3 es el limite sin incluir
print(arregloIndex[3:]) # Empieza desde el 3 hasta el final



print("---------------otra seccion de la numpy indexing----------------")
arregloIndex2 = np.arange(0,11)
arreglo = arregloIndex2[3:6]
print(arreglo)
arreglo[0] = 100 # cambia el valor del elemento 0 del arregloIndex
print(arreglo ) 
print(arregloIndex2) #Se ve cambio en el arregloIndex2 tambien
## para evitar esto se puede usar el metodo copy
print("---------------MÉTODO COPY----------------")
arregloIndex3 = np.arange(0,11)
arreglo3 = arregloIndex3[3:6].copy()
print(arreglo3)
arreglo3[0] = 100
print(arreglo3)
print(arregloIndex3) #No se ve cambio en el arregloIndex3


print("---------------seccion numpy bidemensional-----------------")
arreglobidemensional = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arreglobidemensional)
print(" Muestra fila 0", arreglobidemensional[0])
print(" Muestra numero 1: ", arreglobidemensional[0,0]) #Utilizar mejor esta forma 
print(" Muestra numero 5: ", arreglobidemensional[1][1])

print("---------------seccion numpy bidemensional 2-----------------")
arreglobidemensional2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arreglobidemensional2)
print("...")
#print(arreglobidemensional2[:2,:1]) # Muestra fila 0 y 1
print(arreglobidemensional2[:2,1:]) # Muestra fila 1 y 2 y columna 1 y 2
print("...")
print(arreglobidemensional2[1:,:2]) # Muestra fila 1 y 2 y columna 0 y 1 
print("...")
print(arreglobidemensional2[1:,1:]) # 1 es el limite sin incluir tanto fila como columna

print ("---------------seccion numpy  boolean -----------------")
arreglo = np.arange(0,11)
print(arreglo)
arregloBoolean = arreglo  > 6
print(arregloBoolean)
print(arreglo[arregloBoolean])  # Muestra los numeros mayores que 6 en el arreglo
print(arreglo [arreglo > 7]) #Muestra los numeros mayores que 7 en el arreglo
print("---------------seccion numpy  Ejercicio Prueba -----------------")

arregloEjercicio = np.arange(50).reshape(5,10) # 5 filas y 10 columnas
print(arregloEjercicio) # Muestra el arreglo
print("...")
print(arregloEjercicio[1:3,3:5])  # Muestra fila 1 y 2 y columna 3 y 4 columna los números  13,14,23,24
print("...")

print("---------------seccion numpy  Aritmetica -----------------")
arregloAritmetica = np.arange(0,11)
print(arregloAritmetica) # Muestra el arreglo
 # Eleva al cuadrado cada elemento del arreglo
print(arregloAritmetica **2)
print("...")
# Saca la raiz de cada elemento del arregloAritmetica
print(np.sqrt(arregloAritmetica))
print("...")
# Suma todos los elementos del arregloAritmetica
print(np.sum(arregloAritmetica))
print("...")
# resta todos los elementos del arregloAritmetica
print(np.subtract(arregloAritmetica,5)) # resta 5 a cada elemento del arregloAritmetica
print("...")
# multiplica todos los elementos del arregloAritmetica
print(np.multiply(arregloAritmetica,5)) # multiplica 5 a cada elemento del arregloAritmetica
# divide todos los elementos del arregloAritmetica
print(np.divide(arregloAritmetica,5)) # divide 5 a cada elemento del arregloAritmetica
print("...")
print(np.power(arregloAritmetica,2)) # eleva al cuadrado cada elemento del arregloAritmetica
print("...")
print(np.exp(arregloAritmetica)) # exponencial de cada elemento del arregloAritmetica
print("... funcion log esta comentada la funcion ")
#print(np.log(arregloAritmetica)) # logaritmo de cada elemento del arregloAritmetica
print("... funcion log base 10 esta comentada la funcion")
#print(np.log10(arregloAritmetica)) # logaritmo de 10 de cada elemento del arregloAritmetica
print("...")
print (np.max(arregloAritmetica)) # muestra el numero mas alto del arregloAritmetica
print("...")
print (np.min(arregloAritmetica)) # muestra el numero mas bajo del arregloAritmetica
print("...")
print (np.mean(arregloAritmetica)) # muestra la media de los elementos del arregloAritmetica
print("...")
print (np.median(arregloAritmetica)) # muestra la mediana de los elementos del arregloAritmetica
print("...")
print (np.std(arregloAritmetica)) # muestra la desviacion estandar de los elementos del arregloAritmetica
print("...")
print (np.var(arregloAritmetica)) # muestra la varianza de los elementos del arregloAritmetica
print("...")
print (np.argmax(arregloAritmetica)) # muestra el numero mas alto del arregloAritmetica
print("...")
print (np.argmin(arregloAritmetica)) # muestra el numero mas bajo del arregloAritmetica
print("...")
arregloAritmetica2 = np.arange(0,11)
arregloAritmetica2[0]= 100
print (np.argsort(arregloAritmetica2)) # muestra el indice del arregloAritmetica2 ordenado de menor a mayor 
print("...")
print (np.sort(arregloAritmetica2)) # muestra el arregloAritmetica2 ordenado de menor a mayor




