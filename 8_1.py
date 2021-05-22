
class Data:
    def __init__(self, stroka):
        self.stroka = stroka


    def method_1(self):
        list = (self.stroka).split('-')
        for el in list:
            el = int(el)
            print(el, type(el))

    @staticmethod
    def method_2(ob):
        list = ob.stroka.split('-')
        list1 = [int(el) for el in list]
        if list1[0] <= 0 or list1[0] > 31:
            print('День месяца должнен быть от 1 до 31')
        else:
            print('Число дня месяца корректное')
        if list1[1] <= 0 or list1[1] > 12:
            print('Месяц должен быть от 1 до 12')
        else:
            print('Число месяца корректное')
        if list1[2] <= 0 or list1[2] > 2021:
            print('Год должен быть от 0 до 2021')
        else:
            print('Число года корректное')


d1 = Data('12-01-1988')
d1.method_1()
Data.method_2(d1)
print('*' * 30)
d2 = Data('45-13-20000')
d2.method_1()
Data.method_2(d2)
