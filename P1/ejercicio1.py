import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import math
pxB = np.array ([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 12, 13,
                  14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14])
pyB = np.array ([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                  2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                  10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
pzB = np.array ([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
pB = np.array ([ pxB, pyB, pzB ])
pA = np.copy(pB)



# Apartado a
fig1 = plt.figure ()
ax = fig1.add_subplot (111 , projection ='3d')
ax.title.set_text("Apartado A")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(pA[0],pA[1],pA[2],'.')
#Creo una funcion lambda para calcular rapida la matriz de rotación de x
rx= lambda x:np.asarray([
        [1,0,0],
        [0,math.cos(x*math.pi/180),-math.sin(x*math.pi/180)],
        [0,math.sin(x*math.pi/180),math.cos(x*math.pi/180)]],
        dtype=np.float32)  
#Genero la matriz de rotación de 90º en x
rotacion =rx(90)
#Multiplico todos los puntos por la matriz de rotacion
pB1 = rotacion.dot(pB)
# Pinto la trama rotada
ax.plot(pB1[0],pB1[1],pB1[2],'.')

# Apartado b
fig2 = plt.figure ()
ax1 = fig2.add_subplot (111 , projection ='3d')
ax1.title.set_text("Apartado B")
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.plot(pA[0],pA[1],pA[2],'.')
#Creo una funcion lambda para calcular rapida la matriz de rotación de y
ry= lambda x:np.asarray([
        [math.cos(x*math.pi/180),0,math.sin(x*math.pi/180)],
        [0,1,0],
        [-math.sin(x*math.pi/180),0,math.cos(x*math.pi/180)]],
        dtype=np.float32)  
#Genero la matriz de rotación de 90º en y
rotacion =ry(90)
#Multiplico todos los puntos por la matriz de rotacion
pB2 = rotacion.dot(pB)
# Pinto la trama rotada
ax1.plot(pB2[0],pB2[1],pB2[2],'.')

# Apartado c
fig3 = plt.figure ()

ax2 = fig3.add_subplot (111 , projection ='3d')
ax2.title.set_text("Apartado C")
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.plot(pA[0],pA[1],pA[2],'.')
#Creo una funcion lambda para calcular rapida la matriz de rotación de z
rz= lambda x:np.asarray([
        [math.cos(x*math.pi/180),-math.sin(x*math.pi/180),0],
        [math.sin(x*math.pi/180),math.cos(x*math.pi/180),0],
        [0,0,1]], 
        dtype=np.float32)  
#Genero la matriz de rotación de 90º en z
rotacion =rz(90)
#Multiplico todos los puntos por la matriz de rotación
pB3 = rotacion.dot(pB)
# Pinto la trama rotada
ax2.plot(pB3[0],pB3[1],pB3[2],'.')