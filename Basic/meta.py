# Meta Character
# Tasrif Nur Himel

import re
pattern1 = r"^colo..r$"

if re.match(pattern1,"colouur"):
    print("Matched")
else:
    print("Unmatched")

#(* -------> 0 or more)
pattern2 = r"a*"

if re.match(pattern2,"colouur"):
    print("Matched")
else:
    print("Unmatched")

#(+ -------> 1 or more)
pattern3 = r"a+"

if re.match(pattern3,"colouur"):
    print("Matched")
else:
    print("Unmatched")

#(? -------> 0 or 1)
pattern4 = r"ice(-)?cream"

if re.match(pattern4,"ice--cream"):
    print("Matched")
else:
    print("Unmatched")

#{} ------- range
pattern5 = r"a{1,3}$"

if re.match(pattern5,"aaa"):
    print("Matched")
else:
    print("Unmatched")