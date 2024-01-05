## Take Input From User: 

h = input("Enter number you need: ")
l = h.split()
sum = 0
subs = 0
for x in l:
    sum+=int(x)
    subs-=int(x)
print("The summation is : ",sum)
print("The substraction is : ",subs)