## Number of (Word,letter and digit) of a sentance
## Tasif Nur Himel

word = 0
letter = 0
digit = 0

text = input("Enter a text: ")

for x in text :

    x =  x.lower()
    if x >= 'a' and x <= 'z':
        letter+=1

    elif x >= '0' and x <= '9':
        digit+=1

    elif x == ' ':
        word+=1
print("Number of words: ",word+1)
print("Number of Letters: ",letter)
print("Number of Digits: ",digit)