# Method Overriding
# Tasrif Nur Himel

class phone:
    def __init__(self) -> None:
        print("I am in phone class")

class samsung(phone):
    
    def __init__(self) -> None:
        super().__init__()
        print("I am in Samsung class")

p = samsung()