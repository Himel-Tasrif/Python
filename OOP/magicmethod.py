# Magic Method
# Tasrif Nur Himel

class bike:
    name = ''
    color = ''
    
    def __init__(self,name,color) -> None:
        self.name = name
        self.color = color

    # Magic Method:(Value equal or not check)   
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.color == __value.color
    
    # Magic Method:(value print)  
    def __str__(self) -> str:
        return (f"Name: {self.name}\nColor: {self.color}\n")


    def display(self):
        print(f"Name: {self.name}\nColor: {self.color}\n")

obj1 = bike("R15","Black")
#obj1.display()
obj2 = bike("R15","Black")
#obj2.display()

print(obj1)
print(obj2)

print(obj1 == obj2)

'''there are many magic method like(try those thing):

__add__ magic method
__getitem__ and __setitem__ magic method
__repr__ magic method
__len__ magic method
__lt__, __gt__, __le__, __ge__, __eq__, and __ne__ magic methods
__enter__ and __exit__ magic methods
__call__ magic method
__iter__ magic method'''