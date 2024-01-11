# Queue
# Tasrif Nur Himel

from collections import deque

bank = deque(["Himel", "Rani"])

print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

if not bank:
    print("No member left")