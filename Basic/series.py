## Tasrif Nur Himel 
# Series  (1+2+3+4+..........+n)

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n+1, 1):
    sum += i
print(f"Sum of 1 to {n} is: {sum}")