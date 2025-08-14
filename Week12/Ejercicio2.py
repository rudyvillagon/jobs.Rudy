
from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def calculate_perimeter(self):
        # Perimetro = 2* 3,1415* r Circulo
        # Perimetro = 4*L Cuadrado
        # perimetro = 2 * (Largo + Ancho) Rectangulo
        pass


    @abstractmethod
    def calculate_area(self):
        # Area = 3,1415* r² Circulo
        # Area = L² Cuadrado
        # Area = Largo * Ancho Rectangulo
        pass

import math

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

    def calculate_area(self):
        return math.pi * self.radius ** 2
    

class Square(Shape):

    def __init__(self, side):    
        self.side = side
    

    def calculate_perimeter(self):
        return 4 * self.side
    


    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    


    def calculate_area(self):
        return self.length * self.width
    



circle = Circle(radius = 9)
print("\n==The Perimeter of the Circle ⭕ is:  ")
print(circle.calculate_perimeter())
print("\n==The Area of the circle ⭕ is:  ")
print(circle.calculate_area())


square = Square(side = 5)
print("\n==The Perimeter of the Square 🔳 is:  ")
print(square.calculate_perimeter())
print("\n==The Area of the Square 🔳 is:  ")
print(square.calculate_area())


rectangle = Rectangle(length = 8, width = 4)
print("\n==The Perimeter of the Rectangle 🟩🟩 is:  ")
print(rectangle.calculate_perimeter())
print("\n==The Area of the Rectangle 🟩🟩 is:  ")
print(rectangle.calculate_area())