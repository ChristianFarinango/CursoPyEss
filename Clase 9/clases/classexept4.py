# -*- coding: utf-8 -*-

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(5)
print(exampleObject.a)

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)