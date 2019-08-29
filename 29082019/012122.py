# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:07:14 2019

@author: panch
"""

import numpy as np
#trabajo con valores de arreglos, mascaras
a = np.array([3, -1, -2, 4, -6, 8])

negatives = a < 0 #variable que evalua si valor es negativo o no
print a[negatives] #entrega valores negativos de a
print a[a<0] #entrega valores negativos de a

a[a < 0] = 0 #cambia numero negativos por 0
print a

print (a < 8).any() #si

# & (and), | (or), ~ (not), ^ (xor)
#print (a>3) and (a<8) no funciona
print (a > 3) & (a < 8) #imprime si el valor de la lista cumple esas condiciones

f = 6
g = 9
f + g

print f.__add__(g) #otra forma de sumar variables

print np.nonzero(negatives) #convierte valores negativos a positivos
a.sort() #ordena valores de menor a valor
print a




