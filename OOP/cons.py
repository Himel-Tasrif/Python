# Constructor
# Tasrif Nur Himel

class student:
    name = ''
    age = ''
    id = ''

    def __init__(self,name,age,id) -> None:
        pass
        self.name = name
        self.age = age
        self.id = id

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'ID: {self.id}')

himel = student("Tasrif Nur Himel", 20, "221-35-1078")

himel.display()

#example:(try it must)
'''
class triangle:
    base = ''
    height = ''

    def __init__(self,base,height) -> None:
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height

        print(f"Area of Triangle is: {area}")


t1 = triangle(10,20)
t1.area()
t2 = triangle(20,30)
t2.area() '''