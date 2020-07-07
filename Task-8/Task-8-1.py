class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def transform(cls, data):
        day, month, year = data
        return cls(day, month, year)

    @staticmethod
    def validation(self):

        if self.day > 31 or self.day < 1:
            print("Введите правильный день")

        elif self.month > 12 or self.month < 1:
            print("Введите правильный месяц")

        elif self.year < 0:
            print("Введите правильный год")

chislo = [1, 1, 2020]

my_data = Data.transform(chislo)
print(f"Имеем следующую дату: день - {my_data.day}, месяц - {my_data.month}, год - {my_data.year}")
print(my_data.validation(my_data))


