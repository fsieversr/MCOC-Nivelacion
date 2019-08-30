# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:29:03 2019

@author: panch
"""

#matplotlib
from matplotlib import pyplot as plt #importa libreria

print(plt.style.available) #muestra los estilos

plt.style.use('fivethirtyeight') #aplica estilo

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #valroes eje x

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, 'b', marker = 'o', linewidth=3) #grafica en azul y con marcas y ancho de linea 3

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, 'r', linewidth=3) #grafica en rojo y ancho de linea 3

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #valores y

plt.plot(ages_x, dev_y, 'k--', marker='.' ) #grafica en negro con rayas y marcas

#nombre eje x
plt.xlabel("Ages")
#nombre eje y
plt.ylabel("Median Salary (USD)")
#nombre grafico
plt.title("Median Salary(USD) by Age")
#leyenda tiene que ir en orden
plt.legend(["Python", "JavaScript", "All Devs"])
#agrega grid
plt.grid(True)

plt.tight_layout() #mejora grafico

plt.show() #muestra grafico



