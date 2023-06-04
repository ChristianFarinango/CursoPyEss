# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:12:04 2023

@author: Chris
"""

try:
    x = int(input("Enter the number: "))
    y = 1 / x
    print(y)
    
except ZeroDivisionError:
    print("No se puede dividir para cero")

except ValueError:
    print("tienes que ingresar un numero")
    
except:
    print("algo salió mal")
    
print("End")