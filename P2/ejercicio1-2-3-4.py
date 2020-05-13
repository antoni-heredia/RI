#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:43:47 2020

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
    
#Ejercicio 4 
q1s=np.full(100, np.pi/4)
q2s=np.linspace(0, np.pi/2, 100)
l1 = l2 = 2
dibujar_trayectoria_pcd(q1s,q2s,l1,l2)
