# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:21:57 2019

@author: panch
"""

#IF ELSE STATEMENTS
#se definen variables e y f
e = 20
f = 8
if e < f: #cuando "e" es menor a "f" corre el codigo escrito debajo (imprime la linea siguiente)
    print("e is less than f")
elif e == f: #si no se cumple la primera condicion "if" y ademas "e" es igual a "f" imprime la linea siguiente
    print("e is equal to f")
elif e > f + 10: #si no se cumplen las condiciones anterior y ademas e es mayor a f+10 imprime la linea siguiente 
    print("e is greater than f by more than 10")
else: #cuando no se cumplen las condiciones anteriores imprime la linea siguiente
    print("e is greater less f")