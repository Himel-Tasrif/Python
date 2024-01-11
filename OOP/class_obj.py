# Class and Object
# Tasrif Nur Himel

class student:
    name = ""
    roll = ""
    gpa = ""

himel = student()
print(isinstance(himel,student)) # for check 

himel.name = "Himel"
himel.roll = 101
himel.gpa = 3.85

print(f'Name : {himel.name}' , end=" , ")
print(f'Roll : {himel.roll}' , end=" , ")
print(f'GPA : {himel.gpa}')