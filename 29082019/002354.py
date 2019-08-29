# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:08:36 2019

@author: panch
"""

#Numpy mas completo

import numpy as np

#creacion de arreglos a y b
a = np.array([1, 2, 3, 4])
b = np.array([10, 11, 12, 13])

#se pueden sumar los valores de la lista o cualquier operacion directamente
print a + b 
print a * b 
print a / b


print a.ndim #numero de dimensiones
print a.shape #numero de elementos en cada dimension

#tuplas estan definidas por las comas
f = (5, 6)
print type(f)

print np.sin(a) #el valor de seno de cada uno de los valores de la lista
print np.exp(a) #la funcion exponencial evaluada en cada uno de los valores de a

print a.dtype #imprime tipo de valor qe tiene el arreglo
a = np.array([1, 2, 3, 4.0])
print a.dtype #en este caso el arreglo contiene float, por lo que todo el arreglo es float
#forzar tipo de arreglo
a = np.array([1, 2, 3, 4.0], dtype = "int32")
print a



