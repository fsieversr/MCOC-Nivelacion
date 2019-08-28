# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:16:19 2019

@author: panch
"""

#libreria numpy
#importacion libreria
import numpy as np 
 #libreria para importar fotos
import matplotlib.pyplot as plt #libreria de graficos
from skimage import io

photo = io.imread('ejemplo.jpg')#abre la foto seleccionada ya la guarda como photo


photo_masked = np.where(photo > 100, 255, 0) #si el valor es mayor a 100 es 255, si no es 0
plt.imshow(photo_masked) #muestra la imagen modificada

a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

print a_array + b_array #suma los valores que estan en el mismo lugar de cada array
print a_array + 30 #suma 30 a cada uno de los valores del array
print a_array * b_array #multiplica los valores que estan en la misma posicion en los arrays
print a_array*10 #multiplica cada valor del array por 10
#a_array @ b_array no esta definido el producto punto

plt.imshow(photo[:,:,0].T) #transpone el array

x = np.array([2, 1, 4, 3, 5])
print np.sort(x) #ordena el array de menor a mayor

