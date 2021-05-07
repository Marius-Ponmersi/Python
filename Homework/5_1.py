with open("5_1.txt", "w") as my_fwrite:
    my_fwrite.writelines(
        '\n'.join(input("Введите данные через пробел и нажмите enter: ").split())
    )
