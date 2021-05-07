with open("5_4.txt", "r") as numbers_read:
    numbers = numbers_read.read()
    print(numbers)

with open("5_4_russian.txt", "w+") as f:

    # Функция для замены нескольких значений
    def multiple_replace(target_str, replace_values):
        # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
            # меняем все target_str на подставляемое
            target_str = target_str.replace(i, j)
        return target_str

    # создаем словарь со значениями
    replace_values = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

    # изменяем и печатаем строку
    numbers = multiple_replace(numbers, replace_values)
    print(numbers, file=f)
