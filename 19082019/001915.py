# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:24:12 2019

@author: panch
"""

#variables necesarias para el calculo imc
name = "YK" #nombre persona
height_m = 2 #altura en m
weight_kg = 110. #peso en kg con punto para que tome decimales

bmi = weight_kg / (height_m**2) #formula para calcular imc
print("bmi: ")
print(bmi)
if bmi < 25: #si el imc obtenido es menor a 25 imprime la persona no tiene sobrepeso
    print(name)
    print("is not overweight")
else: #cuando la condicion anterior no se cumple, imprime la persona tiene sobrepeso (unico caso posible imc>25)
    print(name)
    print("is overweight")