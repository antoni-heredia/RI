#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:44:52 2020

@author: antonio
"""

import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1
def pcd ( q1 , q2 , l1 , l2 ):
    y=l1*np.sin(q1)+l2*np.sin(q1+q2)
    x=l1*np.cos(q1)+l2*np.cos(q1+q2)
    return (x,y)
#Ejercicio 3
def dibujar_robot ( q1 , q2 , l1 , l2 ):
    x0 , y0 = 0 , 0; # Pos. de la articulaci ón 1
    x1 , y1 = pcd ( q1 , 0 , l1 , 0); # Pos. de la articulaci ón 2
    x2 , y2 = pcd ( q1 , q2 , l1 , l2 ); # Pos. del extremo del robot
    x = [ x0 , x1 , x2 ]; y = [ y0 , y1 , y2 ]; # Coordenadas de la trayec .
    plt . plot (x , y , 'k'); # Traza la trayectoria
    plt . plot ( x0 , y0 , 'k.'); # Dibuja la articulaci ón 1
    plt . plot ( x1 , y1 , 'k.'); # Dibuja la articulaci ón 2

#Ejercicio 2
def dibujar_trayectoria_pcd (q1s, q2s , l1 , l2 ):
    xs = []
    ys  = []
    for i,q1 in enumerate(q1s):
        x,y = pcd(q1,q2s[i],l1, l2)
        xs.append(x)
        ys.append(y)
    dibujar_robot(q1,q2s[i],l1,l2)
    plt.plot(xs,  ys)
    
#Ejercicio 5
def animacion_trayectoria_pcd ( q1s , q2s , l1 , l2, titulo ):
    n = min(len( q1s ) , len( q2s ))
    fig1 = plt.figure (titulo)
    for i in range (1 , n ):
        plt . clf ()
        dibujar_trayectoria_pcd ( q1s [0: i ] , q2s [0: i ] , l1 , l2 )
        plt.axis([-5,5,-5,5])
        plt . pause (0.001)
        
#Ejercicio 6
q1s=np.linspace(0, np.pi, 101)
q2s=np.linspace(0, np.pi/2, 51)
q2sflip = np.delete(np.flip(q2s),0)
q2s=np.hstack((q2s,q2sflip))
l1 = l2 = 2
animacion_trayectoria_pcd(q1s,q2s,l1,l2,"Ejericio 6")