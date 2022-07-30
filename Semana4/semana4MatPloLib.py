
from operator import index
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import alphas

x = np.linspace(0, 1,11)
y = x**2
plt.plot(x,y,'o') # o es el tipo de grafico 
plt.xlabel('numero')
plt.ylabel('peligro')
plt.title('Primer Gráfico')
#plt.show()

y1 = [1, 7, 3, 4]
x1 = [0, 1, 2, 3]


plt.plot(x1, y1, 'r-') # r- rojo 
plt.grid(True)
plt.axis('tight')
#plt.show()
#graph.show()

#SubPlot tener dos graficas en una 

plt.subplot(1,2,1)
plt.plot(x, y, 'r-') # r- ro
plt.xlabel('número x')
plt.ylabel('peligro y')
plt.title(' Gráfico x')
plt.subplot(1,2,2)
plt.plot(y, x, 'b-') # b- azul
plt.xlabel('número y')
plt.ylabel('peligro x')
plt.title(' Gráfico y')
plt.show()

# Crear una figura 
figura = plt.figure()
axes = figura.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,'r-')
axes.set_xlabel('número x')
axes.set_ylabel('peligro y')
axes.set_title(' Gráfico figura manipulación')
plt.show()

#figura una dentro de otra
fig1 = plt.figure()
ax1 = fig1.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(x,y,'r-')
ax2 = fig1.add_axes([0.7,0.2,0.2,0.2]) #derecha, abajo, ancho, alto
ax2.plot(y,x,'b-')
ax1.set_title('Grande')
ax2.set_title('Chiquito')
# show all active figures (which is now only fig2)
plt.show()

# columnas y filas 

fig,axes3 = plt.subplots(nrows=1, ncols=2) #Vamos a tenr una fila y dos columnas
axes3[0].plot(x,y,'r-')
axes3[0].set_xlabel('número x')
axes3[0].set_ylabel('peligro y')
axes3[0].set_title(' Gráfico 1')
axes3[1].plot(y,x,'b-')
axes3[1].set_xlabel('número y')
axes3[1].set_ylabel('peligro x')
axes3[1].set_title(' Gráfico 2')
plt.show()

fig1,axes4 = plt.subplots(nrows=1, ncols=3) 
pos = 0
for i in axes4: 
    i.plot(x,y,'r-')
    i.set_xlabel('número x')
    i.set_ylabel('peligro y')
    i.set_title(' Gráfico')
    
plt.show()


#figura con subplot
fig2,axes5 = plt.subplots(nrows=2, ncols=1, figsize=(12,4))
axes5[0].plot(x,y,'r-')
axes5[0].set_xlabel('número x')
axes5[0].set_ylabel('peligro y')
axes5[0].set_title(' Gráfico 1')
axes5[1].plot(y,x,'b-')
axes5[1].set_xlabel('número y')
axes5[1].set_ylabel('peligro x')
axes5[1].set_title(' Gráfico 2')
#plt.tight_layout()
plt.show()

# fIGURA CON LEGEND

figura4= plt.figure()
ax = figura4.add_axes([0.1,0.1,.9,.9])
ax.plot(x,y,'r-', label='Grafico 1', linewidth=3, alpha=0.5)
ax.plot(y,x,'b-', label='Grafico 2',linestyle="--" , marker ='o', markersize=5, markerfacecolor='green', markeredgewidth=2, markeredgecolor='black') # ls es el estilo de la linea lw es el grosor alpha es la transparencia marker es el tipo de marcador de cada punto
ax.legend(loc =0) #loc =0 es la posicion de la leyenda en este caso a la izquierda suoperior
figura4.savefig('grafico.png')
plt.show()  



