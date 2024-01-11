#Recursion
# Tasrif Nur Himel

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input("Enter a int number: "))
print(f'The Factorial of {num}! is = {fact(num)}')