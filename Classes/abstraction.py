# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:25:04 2024

@author: vishv
"""

from abc import ABC, abstractmethod
class Polygon(ABC):
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")
        

R = Triangle()
R.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()