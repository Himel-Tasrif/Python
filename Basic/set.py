# Set
# Tasrif Nur Himel

num1 = {1,2,3,4,5,5}
num2 = set([10,11,10])

print(f'Convert list to set: {num2}')

num2.add(2) 
num1.remove(5)

print(f'By adding 2  , now the new set is : {num2}')
print(f'By removing 5 from num1 , now the new set is : {num1}')
print(4 in num1)

# Union 
print(f'Union of num1 and num2 : {num1 | num2}')

# Intersection
print(f'Intersection of num1 and num2 : {num1 & num2}')

# Difference
print(f'Difference of num1 and num2 : {num1 - num2}')