'''
    *
   **
  ***
 ****
*****

solve it:

'''
# Tasrif Nur Himel
n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(n, i, -1):
        print(" ",end = "")

    # for k in range(1, i + 1):
    #     print("*", end="")
        

    print(i*'*')