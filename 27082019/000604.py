# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:57:57 2019

@author: panch
"""

#Libreria Numpy

#importar libreria numpy
import numpy as np
#crea variable de 3 arrays (vectores) igual a 0, con floats decimales
a = np.zeros(3)
#crea variable de 10 arrays (vectores) igual a 0, con floats decimales
z = np.zeros(10)
print z
#vector z queda vertical, 10 valores en 1 columna
z.shape = (10, 1)


z = np.ones(10) #crea vector de unos, 10 en este caso
print z
z = np.empty(3) #crea vector vacio de 3 valores
print z
z = np.linspace(2, 10, 5) #crea vector de 2 a 10 con 5 elementos, todos con la misma diferencia
print z
z = np.array([10, 20]) #crea vector con lista 10 20, tambien se puede poner nombre de lista
print z

np.random.seed(0) #hace que array creado no cambie una vez que se corre
z1 = np.random.randint(10, size = 6) #crea vector aleatorio de 6 valores con numeros hasta el 10 
print z1

print z1[0] #primer valor del vector
print z1[0:2] #valores desde el lugar 0 al 2 del vector
print z1[-1] # ultimo valor del vector


