# Tasrif Nur Himel
#Problem: 1^2 + 2^2 + 3^2 + ........ n^2

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n+1, 1):
    sum += i*i

print(f"Sum of 1^2 to {n}^2 is: {sum}")

'''
Homework:
or factorial
1 x 2 x 3 x 4 x ....... x n

'''