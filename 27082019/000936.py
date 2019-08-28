# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:09:41 2019

@author: panch
"""

#libreria numpy
#importacion libreria
import numpy as np 
 #libreria para importar fotos
import matplotlib.pyplot as plt #libreria de graficos
from skimage import io

photo = io.imread('ejemplo.jpg')#abre la foto seleccionada ya la guarda como photo

#aplicar funciones matematicas a arrays
print(np.sum(photo)) #calcula la suma de los valores
print(np.prod(photo)) #calcula producto de los valores
print(np.mean(photo)) #calcula promedio de los valores
print(np.std(photo)) #desviacion estandar de los valores
print(np.var(photo)) #varianza de los valores
print(np.min(photo)) #minimo de los valores
print(np.max(photo)) #maximo de los valores
print(np.argmin(photo)) #entrega el lugar del valor minimo
print(np.argmax(photo)) #entrega el lugar del valor maximo

