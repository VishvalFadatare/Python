# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:17:07 2024

@author: vishv
"""
#Button
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
button = Button(frame, text='Click me')
button.pack()

root.mainloop()

