# Replace from Regular Expression
# Tasrif Nur Himel

import re
p = r"Himel"
text = "Powerfull people make places powerfull -- Himel"
replc = re.sub(p,'Tasrif',text, count = 1)

print(replc)