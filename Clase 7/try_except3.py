# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:21:11 2023

@author: Chris
"""

try:
    x = int(input("Enter the number: "))
    y = 1 / x
    print(y)
    
except ArithmeticError:
    print("Error aritmetico")

except ZeroDivisionError:
    print("Division por cero")
    
except:
    print("algo salió mal")
    
print("End")