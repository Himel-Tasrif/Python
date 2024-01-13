# Inheritance Example
# Tasrif Nur Himel

class shape:

    v1 = ''
    v2 = ''

    def __init__(self,v1,v2) -> None:
        self.v1 = v1
        self.v2 = v2

    def area(self):
        print("Himel")

class triangle(shape):
    def area(self):
        area = 0.5 * self.v1 * self.v2
        print(f"Area of a triangle: {area}")

class rectangle(shape):
    def area(self):
        area = self.v1 * self.v2
        print(f"Area of a rectangle: {area}")

t = triangle(10,20)
t.area()

r = rectangle(10,20)
r.area()