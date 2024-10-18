# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:32:32 2024

@author: vishval
"""
# it overwrite the data
''' with open("file.txt",'r+') as file1:
    file1.seek(3)
    file1.write("Python program")
    print(file1.read())'''
    
'''with open("file.txt",'w+') as file1:
    file1.write("Python program2")
    print(file1.read())'''
    
'''with open("file.txt",'a+') as file1:
    file1.write("Python program3")
    file1.seek(0)
    print(file1.read())
    file1.close()'''
    
with open("file.txt",'a+') as file1:
    file1.write("Hiii")
    file1.seek(0)
    print(file1.read())
    file1.close()
    

    
    