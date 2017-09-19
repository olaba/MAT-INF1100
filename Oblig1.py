# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:43:19 2017

@author: Ola
"""
#Oblig 1 MATINF - 1100
import numpy as py
import math as ma
import matplotlib.pyplot as plt

#%% Oppgave 1a)
#Deklarerer vektor x og de to første indisiene.
x = py.zeros(100)
x[0] = 1
x[1] = 2

#Lager en forløkke over de hundre verdiene
for i in range(2,100):
    
    #Skriver om ligning (1) og får
    x[i] = 2*x[i-1] + 2*x[i-2]
    print( 2*x[i-1] + 2*x[i-2])


#%% Oppgave 1b)
#Deklarerer vektor x og de to første indisiene.
x = py.zeros(100)
x[0] = 1 
x[1] = 1 - ma.sqrt(3)
    
#Lager en forløkke over de hundre verdiene
for i in range(2,100):
    
    #Skriver om ligning (1) og får
    x[i] = 2*x[i-1] + 2*x[i-2]
    print( 2*x[i-1] + 2*x[i-2])
    
#%% Oppgave 1d)

#Lager vektor med løsningen
xreal = py.zeros(100)
xreal[0] = 1
xreal[1] = 1 - ma.sqrt(3)
for i in range(2,100):
   xreal[i] = (1 - ma.sqrt(3))**i
        
#Regner ut error
err = py.zeros(100)
xx = py.zeros(100)
xx[0] = 1
for i in range(2,100):
       err[i] = ma.log10((x[i] - xreal[i]))
       xx[i] = i
    
#Plotter relativ error
fig1 = plt.figure(2)
h_10 = plt.plot(err)  
plt.title("Error - log10")
plt.ylabel("Error log10")
plt.xlabel("Step number n")
plt.grid()
plt.show()
fig1.savefig('RelativeError.png')
    
#%% 
    
    
