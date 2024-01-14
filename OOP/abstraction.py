# Abstraction
#Tasrif Nur Himel

# calculate area of a triangle, rectangle and circle 

from abc import ABC, abstractmethod
class shape(ABC):   # --------> Abstract Base Class
    num1 = ""
    num2 = ""

    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    @abstractmethod
    def area(self):   # --------> Abstract method 
        pass

class triangle(shape):
    #def __init__(self,num1,num2)

    def area(self):
        area = 0.5 * self.num1 * self.num2
        print(f"Area of a triangle: {area}")

class rectangle(shape):
    #def __init__(self,num1,num2)

    def area(self):
        area = self.num1 * self.num2
        print(f"Area of a rectangle: {area}")

class circle(shape):
    
    def __init__(self, r) -> None:
        super().__init__(r, r)

    def area(self):
        area = 3.14 * self.num1 * self.num2
        print(f"Area of a circle: {area}")


obj1 = triangle(10,20)
#obj1.area()
obj2 = rectangle(10,20)
#obj2.area()
obj3 = circle(10)
#obj3.area()

for i in (obj1,obj2,obj3):
    i.area()
