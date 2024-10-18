# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:16:24 2024

@author: vishval
"""

s=[]
def push():
    if(len(s)==10):
        print('Stack overflow...')
    else:
        a=int(input('Enter element:'))
        s.append(a)
        return s;
    
def pop():
    if(len(s)==0):
        print('Stack Underflow...')
    else:
        ele=s.pop()
        print('Poped element..',ele)
    
def peek():
    e=s[-1]
    print("Top of the stack...",e)
    
def display():
    print('Array',s1)
    
a=1   
while(a!=0):
    print("1:Push 2.Pop 3.Display12 4.Pick 5.Exit")
    ch=int(input('Enter choice:'))
    if(ch==1):
        s1=push();
    elif(ch==2):
        s2=pop();
    elif(ch==3):
        s3=display();
    elif(ch==4):
        s3=peek();
    elif(ch==5):
        a=0