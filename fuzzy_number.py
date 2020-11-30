from math import e

class FuzzyTriangular:
    def __init__(self, a1, a2, a3):
        self.a1, self.a2, self.a3 = a1, a2, a3
    
    def __call__(self, x):
        if x < self.a1:
            return 0
        if x <= self.a2:
            return (x - self.a1) / (self.a2 - self.a1)
        if x <= self.a3:
            return (self.a3 - x) / (self.a3 - self.a2)
        return 0

class FuzzyTrapezoidal:
    def __init__(self, a1, a2, a3, a4):
        self.a1, self.a2, self.a3, self.a4 = a1, a2, a3, a4
    
    def __call__(self, x):
        if x < self.a1:
            return 0
        if x <= self.a2:
            return (x - self.a1) / (self.a2 - self.a1)
        if x <= self.a3:
            return 1
        if x <= self.a4:
            return (self.a4 - x) / (self.a4 - self.a3)
        return 0

class FuzzyBell:
    def __init__(self, mean, deviation):
        self.mean = mean
        self.deviation = deviation
    
    def __call__(self, x):
        return e**(-(x - self.mean)**2 / (2 * self.deviation**2))

class FuzzyPentagonal:
    def __init__(self, a1, a2, a3, a4, a5, w1, w2):
        self.a1, self.a2, self.a3, self.a4, self.a5, self.w1, self.w2 = a1, a2, a3, a4, a5, w1, w2
    
    def __call__(self, x):
        if x < self.a1:
            return 0
        if x <= self.a2:
            return self.w1 * (x - self.a1) / (self.a2 - self.a1)
        if x <= self.a3:
            return self.w1 + (1 - self.w1) * (x - self.a2) / (self.a3 - self.a2)
        if x == self.a3:
            return 1
        if x <= self.a4:
            return 1 - (1 - self.w2) * (x - self.a3) / (self.a4 - self.a3)
        if x <= self.a5:
            return self.w2 * (self.a5 - x) / (self.a5 - self.a4)
        return 0
