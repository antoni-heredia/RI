import numpy as np
import matplotlib.pyplot as plt
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

#Funciones lambda con las que puedes obtener 
#la rotación para cualquiera angulo en cualquier eje
rx= lambda x:np.asarray([
        [1,0,0],
        [0,math.cos(x*math.pi/180),-math.sin(x*math.pi/180)],
        [0,math.sin(x*math.pi/180),math.cos(x*math.pi/180)]],
        dtype=np.float32)  
ry= lambda x:np.asarray([
        [math.cos(x*math.pi/180),0,math.sin(x*math.pi/180)],
        [0,1,0],
        [-math.sin(x*math.pi/180),0,math.cos(x*math.pi/180)]],
        dtype=np.float32)  
rz= lambda x:np.asarray([
        [math.cos(x*math.pi/180),-math.sin(x*math.pi/180),0],
        [math.sin(x*math.pi/180),math.cos(x*math.pi/180),0],
        [0,0,1]], 
        dtype=np.float32)  

primera_r = rx(60)
segunda_r = ry(90)
tercera_r = rz(30)


fig1 = plt.figure ()
ax1 = fig1.add_subplot (111 , projection ='3d')
ax1.title.set_text("1º rotación en X")
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.plot(pA[0],pA[1],pA[2],'.')

pB1 = primera_r.dot(pB)
# Pinto la trama rotada
ax1.plot(pB1[0],pB1[1],pB1[2],'.')


fig2 = plt.figure ()
ax2 = fig2.add_subplot (111 , projection ='3d')
ax2.title.set_text("2º rotación en y")
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.plot(pA[0],pA[1],pA[2],'.')

pB2 = segunda_r.dot(pB1)
# Pinto la trama rotada
ax2.plot(pB2[0],pB2[1],pB2[2],'.')


fig3 = plt.figure ()
ax3 = fig3.add_subplot (111 , projection ='3d')
ax3.title.set_text("3º rotación en z")
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.plot(pA[0],pA[1],pA[2],'.')

pB3 = tercera_r.dot(pB2)
# Pinto la trama rotada
ax3.plot(pB3[0],pB3[1],pB3[2],'.')


#Ahora veremos que pasa si las reotaciones se realizan en otro orden.
fig4 = plt.figure ()

ax4 = fig4.add_subplot (111 , projection ='3d')
ax4.title.set_text("Orden Alterado 1º: Rotación Y")
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
ax4.plot(pA[0],pA[1],pA[2],'.')
fig4.show()
pB1 = segunda_r.dot(pB)
# Pinto la trama rotada
ax4.plot(pB1[0],pB1[1],pB1[2],'.')

fig5 = plt.figure ()
ax5 = fig5.add_subplot (111 , projection ='3d')
ax5.title.set_text("Orden Alterado 2º: Rotación Z")
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('z')
ax5.plot(pA[0],pA[1],pA[2],'.')

pB2 = tercera_r.dot(pB1)
# Pinto la trama rotada
ax5.plot(pB2[0],pB2[1],pB2[2],'.')

fig6 = plt.figure ()
ax6 = fig6.add_subplot (111 , projection ='3d')
ax6.title.set_text("Orden Alterado 3º: Rotación X")
ax6.set_xlabel('x')
ax6.set_ylabel('y')
ax6.set_zlabel('z')
ax6.plot(pA[0],pA[1],pA[2],'.')

pB3 = primera_r.dot(pB2)
# Pinto la trama rotada
ax6.plot(pB3[0],pB3[1],pB3[2],'.')
