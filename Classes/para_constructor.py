# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:35:56 2024

@author: vishv
"""

class Emplyoee:
    def __init__(self,eid,name):
        self.eid=eid
        self.name=name
        
    def display(self):
        print("ID:",self.eid,"\nName:",self.name)
emp=Emplyoee(64, "Vishval")
emp.display()
        
        
        