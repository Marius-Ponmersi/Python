import json
with open('5_7.txt', 'r', encoding='UTF-8') as f_read:
    spisok_strok = f_read.readlines()
    f_read.seek(0)
    content = f_read.read()
    print(content)
    profit_list = []

    for el in spisok_strok:
        profit = float(el.split()[2]) - float(el.split()[3])
        profit_list.append(profit)
    only_profit_list = [float(el) for el in profit_list if el > 0]
    average_profit = sum(only_profit_list) / len(only_profit_list)

    cort = [{el.split()[0]: float(el.split()[2]) - float(el.split()[3])} for el in spisok_strok]
    cort.append({'average_profit': average_profit})
    print(cort)
    print(type(cort))

with open('5_7.json', 'w') as write_f:
    json.dump(cort, write_f)
    json_str = json.dumps(cort)
    print(json_str)
    print(type(json_str))
