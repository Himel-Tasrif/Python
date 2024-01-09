# Tasrif Nur Himel

# Turnary Operator:

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

big = a if( a>b & a>c) else (b if b>c else c)

print(f"The biggest number among three is: {big}")