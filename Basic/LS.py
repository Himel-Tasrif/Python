## Linear Search by
## Tasrif Nur Himel

def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1



number = input("Enter Numbers(using space): ")

l = [int(i) for i in number.split()]

target = int(input("Enter the number you want to search: "))

result = linear_search(l,target)

if (result != -1):
    print("{} value found in {} index ".format(target,result))
else:
    print("Searching value are not found!!!")