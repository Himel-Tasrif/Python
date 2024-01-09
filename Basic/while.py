## Tasrif Nur Himel
## while Loop

'''          Step-1  (Beginner)
i = 1
while i<=10:
    print(i)
    i+=1
print("Program End") ''' 


'''          Step-2  (Mid Level)
def get_loop(z):

    i = 1
    while i<=z:
        print(i)
        i+=1

n = int(input("Enter a value: "))

get_loop(n)
print("Program End")
'''

            #Step-3  (Advance)

def get_loop(z):
    num = []
    i = 1
    while i<=z:
        num.append(i)
        i+=1
    return num
n = int(input("Enter a value : "))

print(*get_loop(n), sep='\n')
print("Program End")