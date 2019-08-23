# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:15:53 2019

@author: panch
"""
#uso de break
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2: #para cada elemento en la lista
    if element <= 0: #si el elemento es negativo rompe el ciclo
        break #rompe el ciclo
    total4 += element
print(total4)

total5 = 0
i= 0
while True: #es siempre verdadero siempre entra al ciclo
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0: #condicion dentro del while
        break #rompe el ciclo cuando el elemento de la lista es negativo
print(total5)


given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total6= 0
j = 0
while j < len(given_list3):
    if given_list3[j] < 0:
        total6 += given_list3[j]
    j += 1
print(total6)