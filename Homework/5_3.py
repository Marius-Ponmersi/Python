with open("5_3.txt", "r", encoding='UTF-8') as salary_read:
    spisok_strok = salary_read.readlines()
    print(spisok_strok)
    for el in spisok_strok:
        if float(el.split()[1]) < 20000.00:
            print((el.split())[0])
    salary = [float(el.split()[1]) for el in spisok_strok]
    print(f"Средняя зарплата: {sum(salary)/len(spisok_strok)}")
