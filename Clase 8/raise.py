# -*- coding: utf-8 -*-

def badFun(n):
    try:
        return n / 0
    except:
        print("Error en cualquier parte")
        raise 
try:
    badFun(0)
except ArithmeticError:
    print("Error lanzado por raise")
print("THE END.")
