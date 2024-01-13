class himel:
    name = ""
    age = ""
    id = ""

    def set_val(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id


    def display(self):
        print(f'My name is: {self.name}')
        print(f'My ID is: {self.id}')
        print(f'My age is: {self.age}\n')

rani = himel()
rani.set_val("Busrat Jahan", 23, "221-35-1111")
rani.display()


h = himel()
h.set_val("Tasrif Nur Himel", 22, "221-35-1078")
h.display()
