# List Input
# Tasrif Nur Himel

n = input("Enter numbers using space: ")

list = n.split()
sum = 0

for x in list:
    sum+=int(x)
print("The sum is: ",sum)