# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:53:09 2019

@author: panch
"""

#Diccionarios

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
