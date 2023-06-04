# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:53:19 2023

@author: Chris
"""

file = open("devices.txt","a")

while True:
    newItem = input("Ingrese un nuevo dispositivo: ")
    
    if newItem == "exit":
        print("All done")
        break

    file.write(newItem + "\n")

file.close()