#Division

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

try:
    div = x/y
    print("Your ans is: ",div)
except Exception as e:
    print("Error Occurs",e)

'''
Do that :

Enter First Number: 10
Enter Second Number: 0

'''