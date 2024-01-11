# Lambda Function(work at single line of code)
# Tasrif Nur Himel


# (a+b)^2 = a*a + 2*a*b + b*b

'''
def cal(a,b):
    return a*a + 2*a*b + b*b

print(f'The result is : {cal(1,2)}')'''

#lambda parameter : argument

x = (lambda a,b : a*a + 2*a*b + b*b)(1,2)

print('The Result is: ',x)