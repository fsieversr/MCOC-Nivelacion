# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:38:54 2019

@author: panch
"""
#numpy en mas dimensiones

import numpy as np

c = np.array([[10, 11, 12], [20, 21, 22]])
print c

print c.ndim #cantidad de dimensiones
print c.shape #muestra la forma, primero filas despues columnas
print c.size #cantidad de valores en arreglo
print c.nbytes #muestra cantidad de memoria que se usa
#toma el primer elemento de la lita, todo en mismo []
print c[0, 0] #fila 0 columna 0
print c[0] #imprime primer elemento, en esta caso primera fila

