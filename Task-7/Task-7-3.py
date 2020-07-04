class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity // cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells_1 = Cell(10)
cells_2 = Cell(5)
print(f"Исходное кол-во клеток №1: {cells_1}")
print(f"Исходное кол-во клеток №2: {cells_2}")
print(f"Сумма клеток №1 и №2: {cells_1 + cells_2}")
print(f"Разница клеток №1 и №2: {cells_1 - cells_2}")
print(f"Умножение клеток №1 и №2: {cells_1 * cells_2}")
print(f"Деление клеток клеток №1 и №2: {cells_1 / cells_2}")
print(f"Формирование ячеек порядам для клетки №1: \n{cells_1.make_order(4)}")
print(f"Формирование ячеек порядам для клетки №2: \n{cells_2.make_order(2)}")
