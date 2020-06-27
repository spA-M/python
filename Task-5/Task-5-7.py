import json
spisok = []
summa = 0
k = 0
pr = {}
with open(r"C:\BIG DATA\Python Projects\Task-5\text_7.txt", "r", encoding="utf-8") as my_file:
    a = my_file.read()
    print(f"Содержимое файла:\n{a}")
    print("")

with open(r"C:\BIG DATA\Python Projects\Task-5\text_7.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        number1 = line.split()
        spisok.append(number1)
        for i in spisok:
            number = line.split()
            name = number[1] + " " + number[0]
            revenue = number[2]
            costs = number[3]
            profit = int(revenue) - int(costs)
        print(f"Прибыль/убыток {name} равна {profit}")

        if profit > 0:
            for j in [profit]:
                summa = summa + j
                k += 1
                aver_profit = summa / k

    print(f"Средняя прибыль компаний равна {aver_profit}")


dic = {}
prof = 0
i = 0
pr = {}

with open(r"C:\BIG DATA\Python Projects\Task-5\text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, firm, earning, cost = line.split()
        dic[name] = int(earning) - int(cost)
        if dic.setdefault(name) >= 0:
            prof = prof + dic.setdefault(name)
            i += 1
            prof_aver = prof / i
            pr = {'средняя прибыль': round(prof_aver)}
    dic.update(pr)
    print(f'Прибыль каждой компании - {dic}')


with open(r"C:\BIG DATA\Python Projects\Task-5\text_77.json", "w", encoding="utf-8") as file_js:
    json.dump(dic, file_js)

    js_str = json.dumps(dic)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')