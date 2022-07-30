
from cmath import e
from pyrsistent import l, s


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


## run elements with the specified key  k1

for elementos in d['k1']:
    ## tomar element with the specified key
        lista = d.items()
        
        for llave, valor in lista:
            val = valor[3]
        
cojo =val.items()
for llave2, valor2 in cojo:
    loco = valor2[3]
resu =loco.items()
for llave3, valor3 in resu:
    resultadoFinal = valor3[3]
    print(resultadoFinal)

print("---------------otra seccion -----------------")
def domainGet(email):
    res = email.split('@')[1]
    return res

prueba = domainGet('user@domain.com')
print(prueba)
print("---------------otra seccion 2-----------------")
def findDog(mensaje):
    if 'dog' in mensaje:
        print('found dog')
        return True
    else:
        print('no dog')
        return False

resultado2 = findDog('Is there a dog here?')
print(resultado2)


print("---------------otra seccion 3-----------------")
def countDog(mensaje):
    contador = mensaje.count('dog')
    return contador
prueba3  =countDog('This dog runs faster than the other dog dude!')
print(prueba3)

print("---------------otra seccion 4-----------------")
seq = ['soup','dog','salad','cat','great']
objetivo ='s'
print(list (filter(lambda x: x[0] == 's', seq)))  

print("---------------otra seccion 5-----------------")
def contiene(seq,objetivo):
    listaEle=[]
    for elemento in seq:
        if elemento[0] == objetivo:
            listaEle.append(elemento)
    return listaEle
  
resultado2 = contiene(seq,objetivo)
print(resultado2)             

print("---------------otra seccion 6-----------------")
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
    if speed <= 60:
        return "No ticket"
    elif speed <= 80 or speed >60:
        return "Small ticket"
    else:
        return "Big ticket"

resultado3= caught_speeding(81,True)    
print(resultado3)       

print ("---------------otra seccion 7-----------------")
## pow de manera más facil
numeropow = 2**3 # 2 elevado a 3
print(numeropow)

print("---------------otra seccion 8 Diccionario-----------------")
# ejercicio diccionarios forma rapida
d1 = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d1['k1'][3]['tricky'][3]['target'][3])





