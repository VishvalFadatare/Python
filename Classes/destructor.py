# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:22:58 2024

@author: vishv
"""

#Destructor 
class Student:
    def __init__(self):
        print("Vishval")
        
    def show(self,name):
        print("Hello",name)
        
    def __del__(self):
        print("Deleted...")
s=Student()
s.show("Vishval")
del s
