# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 09:48:37 2023

@author: Chris
"""

aclNum = int(input("Cual es el numero de la ACL IPv4"))

if aclNum >= 1 and aclNum <= 99:
    print("Estas en una  ACL standard")
    
elif aclNum >= 100 and aclNum <= 199:
    print("Es una ACl estendida")

else:
    print("No es una ACL estardad extendida ni estandar")