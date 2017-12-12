#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:40:26 2016

@author: owais
"""

import pylab as plt

x=[]
y1=[]
y2=[]

for i in range(30):
    x.append(i)
    y1.append(i**3)
    y2.append(1.5**i)
    
plt.figure('Cubic')
plt.clf()
plt.title('Cubic Function')
plt.xlabel('x-vals')
plt.ylabel('y-cbc')
plt.plot(x,y1, 'r--')
 
plt.figure('Expo')
plt.title('Exponential Function')
plt.xlabel('x-vals')
plt.ylabel('y-exp')
plt.plot(x,y2)