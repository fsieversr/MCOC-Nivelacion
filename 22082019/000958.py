# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:50:16 2019

@author: panch
"""
#Loops
#Crear y usar rangos de numeros
c = list(range(1,5)) #crea una lista con rango de numeros que empieza en 1 y no incluye el 5 (1,2,3,4)    
print(c)


total2 = 0
for i in range(1,5): #para cada elemento "i" en el rango entre 1 y 5 (no incluye 5)
    total2 += i #le suma i a total y guarda el nuevo valor
print(total2)


print(list(range(1, 8))) #imprime lista con numeros del 1 al 7

#sumar solo numeros que sean multplos de 3
total3 = 0
for i in range(1, 8): #para cada elemento "i" entre el rango 1 y 7
    #si se puede dividir por 3 que sume al total
    if i % 3 == 0: #operador modulo, entrega el resto de la division
        total3 += i 
print(total3)

#calcular la suma de todos los multiplos de 3 y 5 que sean menor a 100
total4 = 0
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0: #si es multiplo de 3 o de 5 suma al total
        total4 += i
print(total4)