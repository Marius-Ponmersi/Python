spisok = [3, 5, 5, 34, 66, 33, 12, 66, 14, 44, 44, 44]
new_spisok = [el for el in spisok if spisok.count(el) == 1]
print(new_spisok)
