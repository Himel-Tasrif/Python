# xargs and xxargs
# Tasrif Nur Himel

'''
def student(*d):
    print(d)

student(101, "Himel","Rani","Nohan",102)'''

#xargs:
def add(*num):
    sum = 0
    for i in num:
        sum+=i
    print(f'The sum of {num} is : {sum}')
    

add(10,20)
add(10,20,30)
add(10,20,30,40)


#xxargs:
def student(**d):
    print(d)

student(name = "Himel",id = 101)