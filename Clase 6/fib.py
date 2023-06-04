# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:52:45 2023

@author: Chris
"""

def fibonacci(num):
    
    if num == 2:
        return [0, 1]
    
    else:
        secuencia = fibonacci(num - 1)
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        return secuencia
    
lista = fibonacci(8)

for i in lista:
    print(i, end=" ")


    
