# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:53:14 2019

@author: panch
"""

import numpy as np

#slicing de arreglos

#crea arreglo de 25 valores y lo vuelve 5x5
a = np.arange(25).reshape(5,5)
print a

#var[principio:fin(noloincluye):saltos]
red = a[:, 1::2] #toma valores de la columna 1 y 3
print red
yellow = a[-1] #toma valores de la ultima fila
print yellow 
blue = a[1::2 , :-1:2] #toma valores especificos
print blue

red[-1, -1] = 0 #reemplaza valor en red y en a
print red
print a
print red.flags #se puede observar no tiene datos propios depende de otra variable OWNDATA

red1 = red.copy() #vuelve los datos del arreglo como propios
print red1.flags 


