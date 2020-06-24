from functools import reduce

a = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Cписок четных чисел от 100 до 1001: {a}")
proizvedenie = reduce(lambda x, y: x * y, a)

print(f"Результат произведения всех элементов списка: {proizvedenie}")