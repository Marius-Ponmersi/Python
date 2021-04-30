spisok = [12, 45, 23, 536, 34, 4236246, 242, 5475, 37573, 1, 22, 23]

new_spisok = []
for i in range(len(spisok) - 1):
    if spisok[i] < spisok[i + 1]:
        new_spisok.append(spisok[i + 1])
print(new_spisok)

