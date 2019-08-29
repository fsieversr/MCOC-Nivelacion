# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:39:32 2019

@author: panch
"""

import numpy as np
from numpy import loadtext
#arreglos de varias dimensiones
a = np.arange(24).reshape(6, 4) #arreglo de 0 a 24 dimensiones 6 filas 4 columnas
print a
print a.shape
print a.mean(axis=0).shape #axis 0 es columnas, vertical
print a.mean(axis=1).shape #axis 1 es filas, horizontal

channel_means = a.means(axis = 1)

#data = loadtxt('wind.data') importa archivo
#print data.shape inspeccion de cantidad de datos
#dates = data[: , :3] guarda en dates primeras tres columnas de datos
#winds = data[ : , 3:] guarda en winds desde la 3 columna en adelante

#print(winds.mean()m winds.min(), winds.max(), winds.std()) promedio, minimo, maximo, desviacion estandar de datos

#print(winds.min(axis=1)) #muestra el minimo valor de filas

#row = winds.max(axis=1),argmax() #muesra el lugar donde esta el maximo del horizontal

#winds == winds.max() mascara de maximo de winds
#np.where(winds == winds.max()) #tupla donde dice lugar del maximo

#january = dates[:,1] == 1 primera columna cuando el valor sea 1
#print winds[january, :].mean(axis = 0) promedio de la primera columna

