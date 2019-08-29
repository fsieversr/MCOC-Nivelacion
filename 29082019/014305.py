# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:08:59 2019

@author: panch
"""

import numpy as np
#indices en arreglos

a = np.array([10, 1, 20])
b = np.array([2, 3, 20])

subset = a[[0, 2]]
print subset

#analiza si los datos son propios o no
print a.flags.owndata
print subset.flags.owndata

subset[0] = -1 #cambia primer valor de subset
print subset
a[-1] = 100 #cambia ultimo valor de a
print a

#crea arreglo del 0 al 24 y los convierte en una matriz de 5x5
a = np.arange(25).reshape(5, 5)

print a % 3 #muestra el resto de la division por 3 para cada valor del arreglo
print a % 3 == 0 #mascara
print a[a % 3 == 0] #muestra numeros del arreglo que son divisibles por 3

#np.nan #not a number
#nan trabaja con float y arreglo tiene int

output = np.empty_like(a, dtype="float") #crea matriz de forme de a
print output

output.fill(np.nan)  #rellena matriz con nan
print output

mask = a % 3 == 0 #define mascara
output[mask] = a[mask] #reemplaza en el arreglo output los numeros que son divisibles por 9 en a
print output

