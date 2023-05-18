x = 21
loco = "parametro"
palabra = "Hola el numero que va aqui es {uno} que es el {dos}".format(uno=x, dos=loco)
print(palabra)
 
pl = "abcdefghijklmnopqrstuvwxyz"
print(pl[:6])
print ("---------------Parte 1-----------------")
res = "aBcdefas"
## metodos de los arrays
print(res.upper()) # convierte a mayusculas
print(res.lower()) # convierte a minusculas
print(res.capitalize()) # convierte la primera letra a mayuscula
print(res.title()) # convierte la primera letra a mayusculas y las demas a minusculas
print(res.swapcase()) # convierte la letra de acuerdo a su estado actual (mayuscula o minuscula)
print(res.count("a")) # cuenta la cantidad de veces que aparece una letra
print(res.count("A")) # cuenta la cantidad de veces que aparece una letra

print("---------------otra seccion-----------------")
arreglo = [12,22,32]
arreglo.append(21) # agrega un elemento al final del arreglo
print (arreglo)
arreglo.insert(1,5) # insert a new element at the given position
print (arreglo)
arreglo.remove(32) # remove the first element from the list that equals the argument
print (arreglo)
arreglo.pop(1) # remove the element at the given position in the list
print (arreglo)
arreglo.reverse() # reverse the order of the list
print (arreglo)
arreglo.sort() # sort the list in place
print (arreglo)

locura = [1, 2, ["vaIndice2 en el subarray indice 0", "vaIndice2 en el subarray indice 1"] ]
print(locura[2][0])

## Diccionarios en python
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] } # crea un diccionario 

print(diccionario['nombre']) # imprime el valor de la llave nombre

print("---------------otra seccion ciclos-----------------")
## Recorrer un diccionario
for llave in diccionario:
    print(llave)
    print(diccionario[llave])
    if llave == 'cursos':
        for curso in diccionario[llave]:
            print("------>")
            print(curso)
   
## recorrer diccionario con while
print("---------------otra seccion ciclos While-----------------")
i = 0
tam = len(diccionario.keys())
arregloDatos = diccionario.items()
print(tam)
while i < tam:
    ## imprime el valor de la llave
    print(arregloDatos)
    i = i + 1
print(diccionario)
print("---------------otra seccion ciclos 1 -----------------")
for llave, valor in arregloDatos:
    print(llave)
    print(valor)

print("---------------otra seccion ciclos 2 -----------------")
## Recorrer un diccionarios con for  y tuplas
for llave, valor in diccionario.items():
    print(llave)
    print(valor)
    if llave == 'cursos':
        for curso in valor:
            print("------>")
            print(curso)

print("---------------otra seccion agregar -----------------")
## Agregar un elemento al diccionario
diccionario['nuevo'] = 'nuevo valor'
print(diccionario)

print("---------------otra seccion eliminar -----------------")
## Eliminar un elemento del diccionario
del diccionario['nuevo']
print(diccionario)


