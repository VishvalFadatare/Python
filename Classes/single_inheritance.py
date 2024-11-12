# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:44:22 2024

@author: vishv
"""

class A:
    def display(self):
        print("Class A")
        
class B(A):
    def show(self):
        print("Class B")
        
obj=B()
obj.display()
obj.show()