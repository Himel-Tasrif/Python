#Multiple Inheritance
# Tasrif Nur Himel

class A:
    def display1(self):
        print("I am inside A")

class B:
    def display2(self):
        print("I am inside B")

class C(B,A):
    pass
    def display3(self):
        print("I am inside C")

obj1 = C()
obj1.display2()