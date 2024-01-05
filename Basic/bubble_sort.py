## Bubble Sort

def bubble_sort(arr):
     l = len(arr)
     for i in range(l):
          for j in range(0, l-i-1):
               if(arr[j] > arr[j+1]):
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
                 


number = input("Enter elements: ")

n_list = [int(i) for i in number.split()]
print("Unsorted List: ", n_list)

bubble_sort(n_list)

print("Sorted List: ")
for i in range(len(n_list)):
    print("{}".format(n_list[i]), end=" ")
    #print("%d" % n_list[i], end=" ") ------->  you can also use this
