# Join Arrays vertically 
# Tasrif Nur Himel

import numpy as py
a = py.arange(6).reshape(3,2)
b = py.arange(6,12).reshape(3,2)

for i in a:
    print(i)

print("\n")
for i in b:
    print(i)
print("\n")

print(py.vstack((a,b)))