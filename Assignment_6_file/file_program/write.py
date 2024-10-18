# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:25:38 2024

@author: vishval
"""

'''with open("file.txt",'w') as file1:
    file1.write("Hello....")
   
with open("file.txt",'r') as file1: 
   print(file1.read())
   
with open("file.txt",'r') as file2:
    file2.seek(3)
    print(file2.read())
    print(file2.tell())'''
    
with open("file2.txt",'w+') as file1:
    file1.write("Hello new file")
    file1.seek(0)
    print(file1.read())