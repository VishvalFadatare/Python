# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:49:59 2024

@author: vishv
"""

class A:
    def display(self):
        print("Class A")
        
class B:
    def show(self):
        print("Class B")
        
class C(A,B):
    def fun_1(self):
        print("Class C")
        
obj=C()
obj.display()
obj.show()
obj.fun_1()