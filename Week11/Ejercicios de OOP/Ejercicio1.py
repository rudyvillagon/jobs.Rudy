class Circle:
    radius = []


    def __init__(self, radius):
        self.radius = radius
        
        
    
    def get_area(self):
        area_circle = 3.1416*self.radius**2
        print(f"\nThe Area of the Circle ⭕ is {area_circle} cm².\n")

result = Circle(5)
result.get_area()
