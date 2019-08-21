# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:51:12 2019

@author: panch
"""

#Funciones
#Calculadora IMC

#variables necesarias para el calculo imc
name1 = "YK" #nombre persona 1
height_m1 = 2 #altura persona 1 en m
weight_kg1 = 90. #peso en kg persona 1 con punto para que tome decimales

name2 = "YK's sister" #nombre persona 2
height_m2 = 1.8 #altura persona 2 en m
weight_kg2 = 70. #peso en kg persona 2 con punto para que tome decimales

name3 = "YK's brother" #nombre persona 3
height_m3 = 2.5 #altura persona 3 en m
weight_kg3 = 160. #peso en kg persona 3 con punto para que tome decimales

#definicion de funcion para calcular imc
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2) #funcion del imc
    print("bmi: ")
    print(bmi) #imprime el imc
    #condiciones que definen si persona tiene sobrepeso o no
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

#definicion de variables ocupando la funcion con los argumentos de cada persona
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

#imprime la variables, en este caso dicen si tiene sobrepeso o no
print(result1)
print(result2)
print(result3)

