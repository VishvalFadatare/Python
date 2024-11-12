# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:46:28 2024

@author: vishv
"""

class A:
    def display(self):
        print("Class A")
        
class B(A):
    def show(self):
        print("Class B")
        
class C(B):
    def fun_1(self):
        print("Class C")
        
obj=C()
obj.display()
obj.show()
obj.fun_1()