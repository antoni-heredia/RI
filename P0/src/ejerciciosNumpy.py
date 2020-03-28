import numpy as np
import math
#Ejercicio 1
#Un vector con 9 elementos, todos ellos iguales 101.
vector_1 = np.linspace(101,101,9)
#Una matriz de dimensión 4 × 6 con valores aleatorios de acuerdo a una
#distribución normal con media cero y varianza unitaria.
vector_2 = np.random.normal(0,1,[4,6])
#Un vector de 10 elementos con valores aleatorios de números enteros
#entre 4 y 100
vector_3 = np.random.random_integers(4,100,10)
#Una matriz diagonal de dimensión 5 × 5 cuyos elementos de la diagonal
#sean (1, 2, 3, 4, 5).
vector_4 = np.diag(np.linspace(1,5,5))

#Ejercicio 2
a = np.arange(100)
b = a[:20]
c = a[20:]
d = a[-1:-10:-1]
e = a[10:11]
f = a[::-1]
g = a[a% 5 ==0]
h = f[[1,15,60]]

#Ejercicio 3
#Primero generamos todos las filas (que luego se convertirarn en columnas)
primera_final = np.linspace(-1,1,100)

segunda_fila = np.sin(primera_final)

tercera_fila = 1/(1+np.exp(-primera_final))

cuarta_fila = np.copy(segunda_fila)
cuarta_fila[cuarta_fila>0] = 1
cuarta_fila[cuarta_fila<=0] = -1

quinta_fila  = np.random.normal(1,0.5,100)

#Ahora las stackeamos de forma vertical de esta forma tendremos una matriz (5x100)
matriz_final = np.vstack((primera_final,segunda_fila,tercera_fila,cuarta_fila,quinta_fila))
#Ahora realizamos la transpuesta de la anterior matriz quedandonos la matriz 
#100x5 que nos pedian en el enuncaido
matriz_final = matriz_final.T

#extraigo los valores donde el abs(sin(x)) < 0.49
valores_requeridos = matriz_final[abs(np.sin(matriz_final)) < 0.49]

#Calculo cual es el proximo multiplo de 5 para poder crear la matriz con
#el mismo numero de filas
n = 5 - (valores_requeridos.size  % 5)
#Si es necesario creo un vector de tamaño n para poder insertarlo al final del vector de valores
if(n != 5):
    ceros = np.zeros((n,))
    #Concateno el vector de ceros y el de los valores requeridos para que pueda ser
    #multiplo de 5
    valores_requeridos = np.concatenate((valores_requeridos,ceros))

#Combio la forma de vector convirtiendolo en una matriz de 5 columnas
matriz_valores = np.reshape(valores_requeridos,(-1,5))
