class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):
        while True:
            try:

                unit = input(f'Введите наименование офисного оборудования: ')
                unit_p = int(input(f'Введите цену за ед '))
                unit_q = int(input(f'Введите количество '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Текущий список -\n {self.my_store}')
                print(f'Для выхода - Q, продолжение - Enter')

                q = input(f'---> ')
                if q == 'Q' or q == 'q':
                    self.my_store_full.append(self.my_store)
                    print(f'Итого весь склад: \n {self.my_store_full}')
                    return f'Программа завершена'


            except ValueError:
                print(f"Недопустимое значение, вводите только цифры")

class Printer(StoreMashines):
    def to_print(self):
        return f'Принтер печатает {self.numb} листов в минуту'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Сканер сканирует {self.numb} листов в минуту'


class Xerox(StoreMashines):
    def to_copier(self):
        return f'Ксерокс делает {self.numb} ксерокопий в минуту'


unit_1 = Printer('Lenovo', 7000, 50, 1000)
unit_2 = Scanner('HP', 15000, 50, 150)
unit_3 = Xerox('Xerox', 75000, 1, 15000)

print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())

print(unit_1.reception())
