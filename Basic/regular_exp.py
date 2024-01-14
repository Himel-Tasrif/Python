# Regular Expression
# Tasrif Nur Himel

import re
p = r"Himel"  ## For raw string literal

#match method
if re.match(p,"Himel is a good boy"):
    print("Matched")
else:
    print("Not Matched")

#search method
text = "Powerfull people make places powerfull -- Himel"
match = re.search(p,text)
if match:
    print(match.span())
    print(match.group())
    print(match.start())
    print(match.end())
else:
    print("Not Found")

print(re.findall(p,"Himel is a good boy. Himel is a hard working person"))