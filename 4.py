
s = input('Введите несколько слов, разделенных пробелами: ')
l = s.split()
for ind, el in enumerate(l, 1):
    if len(el) > 10:
        print(ind,el[0:10])
    else: print(ind, el)
