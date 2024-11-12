# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:57:01 2024

@author: vishv
"""

import pandas as pd

data = {
  "name": ["Vishval", "Shamal", "Jyoti"],
  "rollno": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 