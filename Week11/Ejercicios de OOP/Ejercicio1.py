class Circle:
    radius = []


    def __init__(self, diameter):
        self.radius = 3.1416*diameter**2
    

    def get_area(self):
        print(f"The Radius is {self.radius}")

result = Circle(5)
result.get_area()
