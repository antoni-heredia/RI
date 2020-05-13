#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:48:21 2020

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


#Ejercicio 7
def pci(x,y,l1,l2):
    q2 = np.arccos((x*x+y*y-l1*l1-l2*l2)/(2*l1*l2))
    #Descomentar segun se quiera usar arctan o arctan2
    #q1 = np.arctan((y*(l1+l2*np.cos(q2))-x*l2*np.sin(q2))/
                   #(x*(l1+l2*np.cos(q2))+y*l2*np.sin(q2)))
    q1 = np.arctan2((y*(l1+l2*np.cos(q2))-x*l2*np.sin(q2)),(
                    x*(l1+l2*np.cos(q2))+y*l2*np.sin(q2)))
    return q1,q2

  
#ejercicio 8
def dibujar_trayectoria_pci(xs, ys , l1 , l2 ):
    q1s = []
    q2s  = []
    for i,x in enumerate(xs):
        q1,q2 = pci(x,ys[i],l1, l2)
        q1s.append(q1)
        q2s.append(q2)
    dibujar_robot(q1,q2,l1,l2)
    plt.plot(xs,  ys)
    
def animacion_trayectoria_pci(xs, ys , l1 , l2, titulo ):
    n = min(len( xs ) , len( ys ))
    fig1 = plt.figure (titulo)
    for i in range (1 , n ):
        plt . clf ()
        dibujar_trayectoria_pci ( xs [0: i ] , ys [0: i ] , l1 , l2 )
        plt.axis([-5,5,-5,5])
        plt . pause (0.001)
        
l1 = l2 = 2
#Ejercicio 9
xs = np.linspace(2,0,100)
ys = np.linspace(0,2,100)
animacion_trayectoria_pci(xs, ys , l1 , l2, "Primer apartado-Eje 9" )

xs = np.linspace(1,-2,100)
ys = np.linspace(1,1,100)
animacion_trayectoria_pci(xs, ys , l1 , l2, "Segundo  apartado-Eje 9" )

xs = np.linspace(1,-1,100)
ys = np.linspace(0,0,100)
animacion_trayectoria_pci(xs, ys , l1 , l2, "Tercer apartado-Eje 9" )
