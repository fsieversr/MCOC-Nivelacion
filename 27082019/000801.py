# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:16:21 2019

@author: panch
"""

#libreria numpy
#importacion libreria
import numpy as np 
 #libreria para importar fotos
import matplotlib.pyplot as plt #libreria de graficos
from skimage import io

photo = io.imread('ejemplo.jpg')#abre la foto seleccionada ya la guarda como photo

plt.imshow(photo) #muestra imagen

plt.imshow(photo[::-1]) #invierte foto porque la corre al reves

plt.imshow(photo[:, ::-1]) #espeja la imagen invierte orden de pixeles

plt.imshow(photo[50:150, 150:280]) #hace zoom en imagen, toma solo cierto rango de los arrays

plt.imshow(photo[::2, ::2]) #toma lineas intercaladas de la imagen
