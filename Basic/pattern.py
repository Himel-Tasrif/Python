
'''
solve it:
*
***
*****
'''
n = int(input("Enter a range: "))

for i in range(n+1):
    print((2*i-1)*"*")


'''

*"*": This part is a string containing a single asterisk (*). 
Multiplying a string by an integer repeats the string that many times. 
So, if (2*i-1) evaluates to 3, it prints three asterisks.
'''