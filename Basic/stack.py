# Stack (LIFO)-----> Last in first Out
# Tasrif Nur Himel
book = []
book.append("C")
book.append("Java")
book.append("Python")
book.append("JavaScript")

print(book)
try:
    book.pop()
    print(f'Stack top: {book[-1]}')
    book.pop()
    print(f'Stack top: {book[-1]}')
    book.pop()
    print(f'Stack top: {book[-1]}')
    book.pop()
    if not book:
        print("No book left")

except Exception as e:
    print(e)
