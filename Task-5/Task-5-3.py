with open(r"C:\BIG DATA\Python Projects\Task-5\text_3.txt", "r", encoding="utf-8") as my_file:
    a = my_file.read()
    print(f"Содержимое файла:\n{a}")
    print("")



with open(r"C:\BIG DATA\Python Projects\Task-5\text_3.txt", "r", encoding="utf-8") as my_file:
    list = my_file.read().split("\n")
    sad_salary = []
    sad_name = []
    salary = []
    summa = 0

    for el in list:
        el = el.split()
        salary.append(el[1])
        new_list = [float(i) for i in salary]


        if float(el[1]) < 20000:
            sad_salary.append(el[1])
            sad_name.append(el[0])
    print(f"Люди у которых оклад меньше 20.000: {sad_name}")

    for j in new_list:
        summa = summa + j
    average_oklad = summa / len(list)

    print(f"Средний оклад работников равен: {average_oklad}")