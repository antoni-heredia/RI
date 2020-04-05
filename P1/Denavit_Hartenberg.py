import numpy as np
import sympy as sp
def algoritmo(parametros):
    #Creo la matriz homogenea como la matriz identidad 
    #para que en la primera multiplicacion no cambie nada
    matriz_homogenea = np.array([[1,0,0,0],
                                 [0,1,0,0],
                                 [0,0,1,0],
                                 [0,0,0,1]])
    for i in parametros:
        i = np.asarray(i).flatten()
        #Ponemos las cuatros matrices, las dos de rotación 
        #y las dos de translacion
        rz = np.array([[sp.cos(i[0]),-sp.sin(i[0]),0,0],
                   [sp.sin(i[0]),sp.cos(i[0]),0,0],
                   [0,0,1,0],
                   [0,0,0,1]])
        dz = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,i[1]],[0,0,0,1]])
        dx= np.array([[1,0,0,i[2]],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        #Realizamos la multiplicaciones para obtener el paso de  i a i+1
        rx = np.array([[1,0,0,0],
                       [0,sp.cos(i[3]),-sp.sin(i[3]),0],
                       [0,sp.sin(i[3]),sp.cos(i[3]),0], 
                       [0,0,0,1]])
        resultado = rz.dot(dz)
        resultado = resultado.dot(dx)
        resultado = resultado.dot(rx)
        
        #Multiplicamos para pasar del 0 a i
        matriz_homogenea = matriz_homogenea.dot(resultado)

    return matriz_homogenea

#Creo los simobolos qeu voy a usar en este ejemplo
q1 , l1,l2, q2, l3, q3 = sp.symbols ('q1,l1,l2,q2,l3,q3')
#Creo la matriz de entrada para el denavit_hatemberg, en este caso de 3x4
entrada = np.array([[q1,l1,0,0],
                    [np.pi/2,q2,0,np.pi/2],
                    [0,l3+q3,0,0]])
#Ejecuto el algoritmo
resultado = algoritmo(entrada)
#Simplifico el resultado
resultado = sp.nsimplify(resultado,tolerance=1e-10)
#Y finalmente lo muestro
print("Los datos de entrada han sido:")
for i in entrada:
    print(i)
print("El resulado han sido:")
#Lo realizo asi para que se vea algo mejor
for i in resultado:
    print(i)

print("---------Otro ejemplo----------")
entrada2 = np.array([[q1,0,l1,0],[q2,0,l2,0]])
resultado2 = algoritmo(entrada2)
resultado2 = sp.nsimplify(resultado2,tolerance=1e-10)
print("Los datos de entrada han sido:")
for i in entrada2:
    print(i)
print("El resulado han sido:")
for i in resultado2:
    print(i)