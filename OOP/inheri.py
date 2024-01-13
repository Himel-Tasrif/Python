# Inheritance
# Tasrif Nur Himel

class phone:
    def call(self):
        print("You can call")
    
    def message(self):
        print("You can message")


class samsung(phone):

    def photo(self):
        print("You can take photo")

p = samsung()
p.call()
p.message()
p.photo()