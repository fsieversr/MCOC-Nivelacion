# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:05:35 2019

@author: panch
"""
#USO  DE IF ELIF ELSE STATEMENTS

#se definen variables a y b
a = 1
b = 2 
if a < b: #cuando "a" es menor a "b" entra al codigo e imprime lo escrito debajo
    print("a is less than b")
    print("a is definitely less than b")
#lo imprime siempre despues de pasar por la condicion
print("Not sure if a is less than b")


#se definen variables c y d
c = 5
d = 4
if c < d: #cuando "c" es menor a "d" corre el codigo escrito debajo (imprime la linea siguiente)
    print("c is less than d")
else:    #cuando no se cumple la condicion anterior imprime lo siguiente
    print("c is NOT less than d")
    print("I don't think c is less than d")
#lo imprime siempre despues de pasar por las condiciones    
print("outside the if block")    

#se definen variables e y f
e = 20
f = 8
if e < f: #cuando "e" es menor a "f" corre el codigo escrito debajo (imprime la linea siguiente)
    print("e is less than f")
elif e == f: #si no se cumple la primera condicion "if" y ademas "e" es igual a "f" imprime la linea siguiente
    print("e is equal to f")
elif e > f + 10: #si no se cumplen las condiciones anterior y ademas e es mayor a f+10 imprime la linea siguiente 
    print("e is greater than f by more than 10")
else: #cuando no se cumplen las condiciones anteriores imprime la linea siguiente
    print("e is greater less f")
    
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

#variables necesarias para el calculo imc
name = "YK" #nombre persona
height_m = 2 #altura en m
weight_kg = 110. #peso en kg

bmi = weight_kg / (height_m**2) #formula para calcular imc
print("bmi: ")
print(bmi)
if bmi < 25: #si el imc obtenido es menor a 25 imprime la persona no tiene sobrepeso
    print(name)
    print("is not overweight")
else: #cuando la condicion anterior no se cumple, imprime la persona tiene sobrepeso (unico caso posible imc>25)
    print(name)
    print("is overweight")





