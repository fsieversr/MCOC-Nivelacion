# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:27:56 2019

@author: panch
"""

#Listas
#definicion de lista con nombre "b"
b = ["banana", "apple", "microsoft"]
#cambio de orden entre banana y microsoft

temp = b[0] #creamos una variable auxiliar para guardar "banana"
b[0] = b[2] #cambiamos banana por microsoft
b[2] = temp #cambiamos microsoft por banana ocupando variable auxiliar

print(b) #imprime lista

#forma para hacerlo mas rapido
b[0], b[2] = b[2] , b[0]
print(b)
