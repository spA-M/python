class My_OwnError(Exception):

    def __init__(self, a, b):
        self.a = a
        self.b = b

a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    c = a / b

except ZeroDivisionError:
    print(f"На ноль делить нельзя")

else:
    print(c)

finally:
    print("Программа завершена")


