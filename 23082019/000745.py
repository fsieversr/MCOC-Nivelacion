# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:56:11 2019

@author: panch
"""

#WHILE

#definimos variable total2
total2 = 0 
j = 1 # se define elemento que analizamos en while
while j < 5: #entra al ciclo cuando j es menor a 5
    total2 += j #suma j al total
    j += 1 #le suma un numero a j
print(total2)

given_list = [5, 4, 4, 3, 1, -2, -3, -5]

total3 = 0
i = 0
while given_list[i] > 0: #entra al ciclo cuando el elemento de la lista es mayor a 0 
    total3 += given_list[i] #le suma al total el elemento i de la lista
    i += 1 #hace que vaya al siguiente elemento de la lista
print(total3)


#si la lista tiene solo numero positivos es error
given_list1 = [5, 4, 4, 3, 1]
total4 = 0
k = 0
while k < len(given_list1) and given_list1[k] > 0: #entra al ciclo cuando el elemento es positivo y k es menor al largo de la lista
    total4 += given_list1[k] #le suma al total el elemento i de la lista
    k += 1 #hace que vaya al siguiente elemento de la lista
print(total4)

