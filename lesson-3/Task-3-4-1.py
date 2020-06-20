x = int(input('Введите число x: '))
y = int(input('Введите степень y: '))


def my_func(x, y):
    if x > 0 and y < 0:
        stepen = abs(y)
        num = 1
        while stepen > 0:
            num *= x
            stepen -= 1
            final = 1 / num
        return final
    else:
        print("Х - должно быть целым числом больше нуля, а Y - целым числом меньше нуля, повторите ввод")

print(f'Результат возведения в степень равен: {my_func(x, y)}')
