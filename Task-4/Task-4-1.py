from sys import argv
script_name, hours, stavka, premia = argv

print("Имя скрипта: ", script_name)
print("Кол-во отработанных часов: ", hours)
print("Ставка в час: ", stavka)
print("Премия: ", premia)

a = int(hours)
b = int(stavka)
c = int(premia)

def zp():
    try:
        salary = (a * b) + c

    except ValueError:
        print("Введите цифры, а не буквы")
    return salary

print(f"Зарплата работника равна: {zp()}")