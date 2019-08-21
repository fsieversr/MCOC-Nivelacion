# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:19:47 2019

@author: panch
"""

#Listas
#variable definida con lista
a = [3, 10, -1]
print(a)

#agregar item (numero) a lista
a.append(1)
print(a)

#agregar string a lista
a.append("hello")
print(a)

#agregar lista a lista
a.append([1,2])
print(a)

#sacar ultimo item de la lista
a.pop()
print(a)

#sacar item especifico de la lista 
#listas empiezan en posicion cero
print(a[0]) #imprime primer item de la lista

#cambiar valor de la lista
a[0]=100
print(a)

