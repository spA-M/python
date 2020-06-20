def devision():

    a = input("Введите число, которое будет являться делимым: ")
    b = input("Введите число, которое будет являться делителем: ")
    try:
        a = int(a)
        b = int(b)
        c = a / b

    except ValueError:
        print("Введите цифры, а не буквы")

    except ZeroDivisionError:
        print("Делитель не должен равняться нулю")
    return c
print(f'Результат деления равен: {round(devision(),2)}')