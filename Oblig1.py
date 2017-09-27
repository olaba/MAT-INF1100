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
    
#%% Oppgave 2a)

#initialiserer variablene i og n    
n = [5000.0,100000.0,1000.0]
i = [4.0,60.0,500.0]

#lager en forløkke over de tre tilfelle
for t in range (0,3):
    
    #initialiserer den første binomialkoeffisienten
    binom = (i[t]+1.0)
    
    #Kalkulerer binomialkoeffisient. Får med siste multiplikasjon ved +1! 
    for j in range (2,(int(n[t]-i[t]) + 1)):
        
        binom = binom*((i[t]+float(j))/float(j))

    print(binom)


#%% Oppgave 3b)

from random import random

antfeil = 0; N = 10000
x0 = y0 = z0 = 0.0
feil1 = feil2 = 0.0

for i in range(N):
    x = random(); y = random(); z = random()
    res1 = x*(y + z)
    res2 = x*y + y*z
    
    if res1 != res2:
        antfeil += 1
        x0 = x; y0 = y; z0 = z
        ikkeass1 = res1
        ikkeass2 = res2
        
print (100. * antfeil/N)
print (x0, y0, z0, ikkeass1 - ikkeass2)
    
    
