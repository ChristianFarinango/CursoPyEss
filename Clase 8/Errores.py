# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:46:19 2023

@author: Chris
"""

def readint(prompt, minv, maxv):
    while True:   
        try:
            valor = int(input(prompt))
            if (valor >= maxv):
                print("El valor no esta dentro del rango")
    
            elif valor <= minv:
                print("El valor no esta dentro del rango")
            else:
                return valor
        except:
            #print("error en el ingreso")
            print("error en el ingreso")
            


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
