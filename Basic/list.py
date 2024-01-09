# List and it's function
# Tasrif Nur Himel

h = [3,2,0,1,5,4]
print(f"The value of 2 no index is : {h[2]}")

# for last value just type [-1]
print(f"The last value of the list is: {h[-1]}")

# IN and NOT IN operator--------> return boolean
print("3" in h)
print("3" not in h)

# Add something using Append 
h.append(7)
print("Current List: ", h)
'''
when we use append it now make a new list which is h = [1,2,3,4,5,6,7]
'''

# Lenght of list and it's count start from 1
print(f"Length of the current list : {len(h)}")

#Add ---- another way
print(h + ["Himel", "Rani", 33, 66])


#Insert function
h.insert(2,2000)
print(h)

#Remove function
h.remove(2000)
print(h)

# Sort Function (By default ascending order)
h.sort()
print(h)

# Reverse function for descending order :
h.reverse()
print(h)

# POP function -----> remove last value
h.pop()
print(h)

# Copy list
h1 = h.copy()
print(h1)

# Clear
h.clear()
print(h)

#INDEX find the position
print(h1.index(3)) # Which values index you want to see

# Count
print(h1.count(3)) # how many 3 in you list 