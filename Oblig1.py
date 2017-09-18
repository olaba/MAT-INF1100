# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:43:19 2017

@author: Ola
"""
#Oblig 1 MATINF - 1100
import numpy as py
import math as ma

#Oppgave 1 - a)
#Deklarerer vektor x og de to første indisiene.
x = py.zeros(100)
x[0] = 1
x[1] = 2

#Lager en forløkke over de hundre verdiene
for i in range(2,100):
    
    #Skriver om ligning (1) og får
    x[i] = 2*x[i-1] + 2*x[i-2]
    print( 2*x[i-1] + 2*x[i-2])


print("--------------")

#Oppgave 1 - b)
#Deklarerer vektor x og de to første indisiene.
x = py.zeros(100)
x[0] = 1 - ma.sqrt(3)
x[1] = 2
    
#Lager en forløkke over de hundre verdiene
for i in range(2,100):
    
    #Skriver om ligning (1) og får
    x[i] = 2*x[i-1] + 2*x[i-2]
    print( 2*x[i-1] + 2*x[i-2])
    
    
    
