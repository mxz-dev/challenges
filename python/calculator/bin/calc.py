class Calc: # calculator object
    def __init__(self, x,y):
        self.result = 0
        self.x = x # first number 
        self.y = y # second number
    def add(self):
        self.result = self.x + self.y
        return self.result
    def subtract(self):
        self.result = self.x - self.y
        return self.result
    def multiply(self):
        self.result = self.x * self.y
        return self.result
    def division(self):
        self.result = self.x / self.y
        return self.result
