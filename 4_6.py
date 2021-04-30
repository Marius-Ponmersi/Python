from itertools import count
from itertools import cycle

for el in count(9):
    if el > 20:
        break
    else:
        print(el)

print("*" * 50)

spisok = [1, 54, "asd", True]
c = 0
for el in cycle(spisok):
    if c > 15:
        break
    else:
        print(el)
    c = c + 1
