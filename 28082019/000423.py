#importamos la libreria numpy
import numpy as np

#creamos un array en numpy con 3 elementos
a = np.array([2,3,4])
print a

#creamos un array con elemento entre el 1 y el 12 en intervalos de 2
a = np.arange(1,12,2)
print a

#creamos un array de 1 a 12 con 6 elementos
a = np.linspace(1,12,6)
print a

#ahora ordenamos el arreglo anterior en un array de 2 dimensiones
a = a.reshape(3,2)
print a

#vemos el numero de elementos sin importar la dimension que tenga el arreglo
print a.size

#mostramos las dimensiones del arreglo
print a.shape

#mostramos el tipo de datos que tiene el arreglo
print a.dtype

#mostramos la memoria utilizada (en bites)
print a.itemsize

#ahora creamos manualmente un arreglo de 2 dimensiones
b = np.array([(1.5,2,3), (4,5,6)])

#comparamos que cada elemento de "a" sea menor que 4 y nos entrega un arreglo con booleanos
print a < 4

#ahora multiplicamos el arreglo entero por 3
print a * 3

#creamos un arreglo de la dimension que queramos llena de ceros
a = np.zeros((3,4))
print a

#creamos un arreglo de la dimension que queramos llena de unos
a = np.ones((2,3))
print a

#agrega tipo de dato, sirve para determinar uso de memoria
a = np.array([2,3,4],dtype=np.int16)
print a

#matriz de 2x3 de numeros random entre 0 y 1
a = np.random.random((2, 3))

#configura imprimicion numpy, especificamentw cantidad de decimales
np.set_printoptions(precision=2, suppress = True)
print a

#numeros enteros 5 numeros aleatorios entre 0 y 10
a = np.random.randint(0, 10, 5)
#suma valores de a
print a.sum()
#maximo
print a.max()
#minimo
print a.min()
#promedio
print a.mean()
#varianza
print a.var()
#desviacion estandar
print a.std()

#array de 6 integros
a = np.random.randint(1, 10, 6)
#cambia dimensiones arreglo
a = a.reshape(3,2)
#suma en linea horizontal
print a.sum(axis=1)
#suma vertical
print a.sum(axis=0)