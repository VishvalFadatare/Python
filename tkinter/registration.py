# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:41:06 2024

@author: vishv
"""

import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Registration Form")
window.geometry("350x300")

# Username label and text entry box
label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Email label and text entry box
label_email = tk.Label(window, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Password label and text entry box
label_password = tk.Label(window, text="Password:")
label_password.grid(row=2, column=0, padx=10, pady=10)
entry_password = tk.Entry(window, show='*')
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Confirm Password label and text entry box
label_confirm_password = tk.Label(window, text="Confirm Password:")
label_confirm_password.grid(row=3, column=0, padx=10, pady=10)
entry_confirm_password = tk.Entry(window, show='*')
entry_confirm_password.grid(row=3, column=1, padx=10, pady=10)

# Gender label
label_gender = tk.Label(window, text="Gender:")
label_gender.grid(row=4, column=0, padx=10, pady=10)

# Gender radio buttons
gender_var = tk.StringVar(value="Male")  # Default selection

radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
radio_male.grid(row=4, column=1, sticky='w')

radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
radio_female.grid(row=5, column=1, sticky='w')

# Register button (no functionality)
button_register = tk.Button(window, text="Register")
button_register.grid(row=6, column=1, pady=20)

# Run the application
window.mainloop()
