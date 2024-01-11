# Reading and Writting file
# tasrif Nur Himel

# File Read
h = open('file.txt','r+') # open('file.txt','w')
print(h.readable()) # print(h.writable())
l = h.readlines()  # Convert into list
r = h.read()

print(r)
print(len(r))
print(l)


#Write file (Please create a extra python file for better result)
file = open("file.txt", "a")

file.write("\nI am a good boy")