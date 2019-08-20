# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:22:45 2019

@author: panch
"""

#IF ELSE STATEMENTS

#se definen variables "g" y "h"    
g = 9 
h = 8 
if g < h: #cuando "g" es menor a "h" corre el codigo escrito debajo (imprime la linea siguiente)
    print("g is less than h")
else: #cuando no se cumple el "if" anterior corre lo escrito debajo
    if g == h: #cuando g y h son iguales corre codigo escrito debajo
        print("g is equal to h")
    else: #cuando no se cumple que son iguales corre el codigo escrito debajo
        print("g is greater than h")