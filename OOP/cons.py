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