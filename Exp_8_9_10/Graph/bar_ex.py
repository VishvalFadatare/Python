# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:17:46 2024

@author: vishv
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()