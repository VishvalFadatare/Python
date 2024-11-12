# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:48:03 2024

@author: vishv
"""

class A:
    def display(self):
        print("Class A")
        
class B(A):
    def show(self):
        print("Class B")
        
class C(A):
    def fun_1(self):
        print("Class C")
obj1=B()
obj1.display()
obj1.show()      
obj=C()
obj.display()
obj.fun_1()