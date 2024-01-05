n = input("Enter a text of numbers: ")

list = n.split()
sum = 0

for x in list:
    sum+=int(x)
print("The sum is: ",sum)