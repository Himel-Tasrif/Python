# Multi-level Inheritance
# Tasrif Nur Himel

class A:
    def display1(self):
        print("I am inside A")

class B(A):
    def display2(self):
        print("I am inside B")

class C(B):
    def display3(self):
        print("I am inside C")

obj1 = C()
obj1.display1()
obj1.display2()
obj1.display3()