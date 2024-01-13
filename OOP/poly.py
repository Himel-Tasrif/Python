# Polymorphism
# Tasrif Nur Himel

class car:
    brand = ''
    model = ''

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print("Drive\n")

class boat:
    brand = ''
    model = ''

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Boat Brand: {self.brand}")
        print(f"Boat Model: {self.model}")
        print("Sail\n")

class plane:
    brand = ''
    model = ''

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Plane Brand: {self.brand}")
        print(f"Plane Model: {self.model}")
        print("Fly\n")

car1 = car("Ford", "Mustang") 
#car1.move()
boat1 = boat("Ibiza", "Touring 20")
#boat1.move()
plane1 = plane("Boeing", "747")  
#plane1.move() 

for i in (car1,boat1,plane1):
      i.move()