with open("5_2.txt", "r") as f_read:
    spisok_strok = f_read.readlines()
    print(spisok_strok)
    print(f"Количество строк в файле: {len(spisok_strok)}")
    f_read.seek(0)
    n = 1   # номер строки
    for line in f_read:
        print(f"Количество слов в {n} строке: {len(line.split())}")
        n += 1
