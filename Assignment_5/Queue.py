# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:47:58 2024

@author: vishval
"""

s=[]
def enqueue():
    if(len(s)==10):
        print('Queue overflow...')
    else:
        a=int(input('Enter element:'))
        s.append(a)
        return s;
    
def dequeue():
    if(len(s)==0):
        print('Queue is underflow...')
    else:
        ele=s.pop(0)
        print('Deleted element..',ele)
    
def peek():
    e=s[-1]
    e1=s[0]
    print("Front of the Queue...",e)
    print("Rear of the Queue...",e1)
    
def display():
    print('Array',s1)
    
a=1   
while(a!=0):
    print("1:Enqueue 2.Dequeue 3.Display12 4.Pick 5.Exit")
    ch=int(input('Enter choice:'))
    if(ch==1):
        s1=enqueue();
    elif(ch==2):
        s2=dequeue();
    elif(ch==3):
        s3=display();
    elif(ch==4):
        s3=peek();
    elif(ch==5):
        a=0