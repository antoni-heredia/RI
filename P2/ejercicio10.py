#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:44:43 2020

@author: antonio
"""

import numpy as np
import matplotlib.pyplot as plt
def pcd ( q1 , q2 , l1 , l2 ):
    y=l1*np.sin(q1)+l2*np.sin(q1+q2)
    x=l1*np.cos(q1)+l2*np.cos(q1+q2)
    return (x,y)
def dibujar_robot ( q1 , q2 , l1 , l2 ):
    x0 , y0 = 0 , 0; # Pos. de la articulaci ón 1
    x1 , y1 = pcd ( q1 , 0 , l1 , 0); # Pos. de la articulaci ón 2
    x2 , y2 = pcd ( q1 , q2 , l1 , l2 ); # Pos. del extremo del robot
    x = [ x0 , x1 , x2 ]; y = [ y0 , y1 , y2 ]; # Coordenadas de la trayec .
    plt . plot (x , y , 'k'); # Traza la trayectoria
    plt . plot ( x0 , y0 , 'k.'); # Dibuja la articulaci ón 1
    plt . plot ( x1 , y1 , 'k.'); # Dibuja la articulaci ón 2

#Ejercicio 10
def pci2(x,y,l1,l2):
    
    q2_1 = np.arccos((x*x+y*y-l1*l1-l2*l2)/(2*l1*l2))
    q2_2 = -q2_1
    
    q1_1 = np.arctan2((y*(l1+l2*np.cos(q2_1))-x*l2*np.sin(q2_1)),
                      (x*(l1+l2*np.cos(q2_1))+y*l2*np.sin(q2_1)))
    q1_2 = np.arctan2((y*(l1+l2*np.cos(q2_2))-x*l2*np.sin(q2_2)),
                      (x*(l1+l2*np.cos(q2_2))+y*l2*np.sin(q2_2)))
    
    return (q1_1,q1_2,q2_1,q2_2)     

def dibujar_trayectoria_pci2(xs, ys , l1 , l2 ):
    q1s = []
    q2s  = []
    for i,x in enumerate(xs):
        q1_1,q1_2,q2_1,q2_2 = pci2(x,ys[i],l1, l2)
        
        if(len(q1s) > 0):
            if(abs(q1s[-1]-q1_1)<abs(q1s[-1]-q1_2)):
                q1s.append(q1_1)
                q2s.append(q2_1)
            else:
                q1s.append(q1_2)
                q2s.append(q2_2)
        else:
            q1s.append(q1_1)
            q2s.append(q2_1)



    dibujar_robot(q1s[-1],q2s[-1],l1,l2)
    plt.plot(xs,  ys)
    
def animacion_trayectoria_pc2i(xs, ys , l1 , l2,titulo ):
    n = min(len( xs ) , len( ys ))
    fig1 = plt.figure (titulo)
    for i in range (1 , n ):
        plt . clf ()
        dibujar_trayectoria_pci2 ( xs [0: i ] , ys [0: i ] , l1 , l2 )
        plt.axis([-5,5,-5,5])
        plt . pause (0.001)
        
l1 = l2 = 2

#Probamos el ejercicio 10
xs = np.linspace(1,-2,100)
ys = np.linspace(1,1,100)
animacion_trayectoria_pc2i(xs, ys , l1 , l2, "Segundo  apartado-Eje 10" )
xs = np.linspace(1,-1,100)
ys = np.linspace(0,0,100)
animacion_trayectoria_pc2i(xs, ys , l1 , l2, "Tercer apartado-Eje 10" )
