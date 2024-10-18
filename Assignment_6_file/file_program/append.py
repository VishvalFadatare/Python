# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:30:02 2024

@author: vishval
"""

with open("file.txt",'a') as file1:
    file1.write("Python Programming")
    print("Appended successfully...")
    
with open("file.txt",'r') as file1:
    print(file1.read())
    file1.close()
    
    