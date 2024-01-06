# Bigest Number among three
# Tasrif Nur Himel

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    if a>c:
        print("The Bigest number is ",a)
    else:
        print("The Bigest number is ",c) 

elif b>a:
    if b>c:
        print("The Bigest number is ",b) 
    else:
        print("The Bigest number is ",c) 