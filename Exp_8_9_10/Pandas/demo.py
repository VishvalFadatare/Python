# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:49:00 2024

@author: vishv
"""

import pandas as pd

mydata = {
  'name': ["Vishval", "Shamal", "Namrata"],
  'rollno': [64, 62, 66]
}

myvar = pd.DataFrame(mydata)

print(myvar)