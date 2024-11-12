# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:42:58 2024

@author: vishv
"""

import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("270x300")

entry_display = tk.Entry(window, font=("Arial", 16), borderwidth=2, relief="ridge", justify='right')
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_7 = tk.Button(window, text='7', padx=15, pady=15, font=('Arial', 12))
button_7.grid(row=1, column=0)

button_8 = tk.Button(window, text='8', padx=15, pady=15, font=('Arial', 12))
button_8.grid(row=1, column=1)

button_9 = tk.Button(window, text='9', padx=15, pady=15, font=('Arial', 12))
button_9.grid(row=1, column=2)

button_div = tk.Button(window, text='/', padx=15, pady=15, font=('Arial', 12))
button_div.grid(row=1, column=3)

button_4 = tk.Button(window, text='4', padx=15, pady=15, font=('Arial', 12))
button_4.grid(row=2, column=0)

button_5 = tk.Button(window, text='5', padx=15, pady=15, font=('Arial', 12))
button_5.grid(row=2, column=1)

button_6 = tk.Button(window, text='6', padx=15, pady=15, font=('Arial', 12))
button_6.grid(row=2, column=2)

button_mul = tk.Button(window, text='*', padx=15, pady=15, font=('Arial', 12))
button_mul.grid(row=2, column=3)

button_1 = tk.Button(window, text='1', padx=15, pady=15, font=('Arial', 12))
button_1.grid(row=3, column=0)

button_2 = tk.Button(window, text='2', padx=15, pady=15, font=('Arial', 12))
button_2.grid(row=3, column=1)

button_3 = tk.Button(window, text='3', padx=15, pady=15, font=('Arial', 12))
button_3.grid(row=3, column=2)

button_sub = tk.Button(window, text='-', padx=15, pady=15, font=('Arial', 12))
button_sub.grid(row=3, column=3)

button_clear = tk.Button(window, text='C', padx=15, pady=15, font=('Arial', 12))
button_clear.grid(row=4, column=0)

button_0 = tk.Button(window, text='0', padx=15, pady=15, font=('Arial', 12))
button_0.grid(row=4, column=1)

button_equal = tk.Button(window, text='=', padx=15, pady=15, font=('Arial', 12))
button_equal.grid(row=4, column=2)

button_add = tk.Button(window, text='+', padx=15, pady=15, font=('Arial', 12))
button_add.grid(row=4, column=3)

window.mainloop()


