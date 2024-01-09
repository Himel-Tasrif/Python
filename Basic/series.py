## Tasrif Nur Himel 
# Series  (1+2+3+4+..........+n)

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n+1, 1):
    sum += i
print(f"Sum of 1 to {n} is: {sum}")

'''
Homework:
2+4+6+8+.......+n 

note one thing series depends on 3 things:
1. range start with
2. range end with
3. distance between one from another

'''