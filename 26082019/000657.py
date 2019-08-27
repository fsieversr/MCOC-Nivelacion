# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:01:46 2019

@author: panch
"""

#definicion de variable que contenga diccionario
d = {}
d["George"]= 24 #agrega al diccionario George: 24
d["Tom"] = 32 #agrega al diccionario Tom: 32
d["Jenny"]= 16 #agrega al diccionario Jenny 16

print(d["George"]) #imprime el valor asociado con George
print(d["Tom"])  #imprime el valor asociado con Tom

d["Jenny"] = 20  #cambia el valor asociado a Jenny
print(d["Jenny"]) #imprime el valor asociado a Jenny
#si uno escribe el nombre incorrecto imprime error
print("") #imprime una espacio

d[10] = 100 #agrega al diccionario un key 10 con valor 100

#iteracion en el valor de los keys
for key, value in d.items(): #para cada key en 
    print("key:") #imprime "key"
    print(key) #imprime el item key de d(George, Jenny, etc)
    print("value:") #imprime "value"
    print(value) #imprime el valor asociado al key
    print("") #imprime una espacio
    