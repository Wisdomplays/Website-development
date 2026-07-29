class circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of circle =", round(area, 2))

    def perimeter(self):
            perimeter = 2 * 3.14 * self.radius
            print("Perimeter of circle =", round(perimeter, 2))
    
    