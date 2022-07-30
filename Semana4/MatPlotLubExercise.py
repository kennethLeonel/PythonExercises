import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
import matplotlib.pyplot as plt 
#%matplotlib inline # para que muestre en el Jupyter notebook

#Ejercicio 1
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('grafico')
plt.show()

#Ejercicio 2
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax.plot(x,y)
ax2.plot(x,y)
plt.show()

#Ejercicio 3
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax.plot(x,z)
ax2.plot(x,y)
plt.xlim(20,22),
plt.ylim(30,50)
plt.show()

#Ejercicio 4
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y,color='blue',lw =3, ls ='--')
axes[1].plot(x,z,color='red',lw =3)
plt.show()

#Ejercicio 5
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))
axes[0].plot(x,y,color='blue',lw =4 )
axes[1].plot(x,z,color='red',lw =3, ls ='--')
plt.show()

