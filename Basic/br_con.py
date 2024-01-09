## Break and Continue:
#Tasrif Nur Himel

## Break:(Try this must)
'''
i = 1
while i <= 100:
    print(i)
    i+=1

    if i == 5:
        break
print("The Program is close")'''

## Continue: (Try this must)
'''
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)
'''

# Combine:
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
    
    if i == 7:
        break  # Terminate the loop when i becomes 7
    
