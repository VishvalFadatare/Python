# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:18:47 2024

@author: vishv
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 