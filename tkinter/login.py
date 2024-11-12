# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:34:37 2024

@author: vishv
"""

import tkinter as tk

# Initialize the main m
m = tk.Tk()
m.title("Login Form")
m.geometry("300x150")

# Username label and text entry box
label_username = tk.Label(m, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(m)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password label and text entry box
label_password = tk.Label(m, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(m, show='*')
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Login button (no functionality)
button_login = tk.Button(m, text="Login")
button_login.grid(row=2, column=1, pady=20)

m.mainloop()
