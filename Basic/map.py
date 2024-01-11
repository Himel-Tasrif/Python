# Map & Filter
# Tasrif Nur Himel

def squre(x):
    return x*x


num = [1,2,3,4,5]

y = list(map(squre,num))

print(f'Squre of all list values: {y}')


# Filter

result = list(filter(lambda i: i%2==00, num))

print(f'Even number from {num} are: {result}')