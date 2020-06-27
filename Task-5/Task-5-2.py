with open(r"C:\BIG DATA\Python Projects\Task-5\Text-2.txt", "r", encoding="utf-8") as my_file:
    a = my_file.read()
    print(f"Содержимое файла:\n{a}")
    print("")

with open(r"C:\BIG DATA\Python Projects\Task-5\Text-2.txt", "r", encoding="utf-8") as my_file:
    for ind, line in enumerate(my_file.readlines(), 1):
        a = line.split()
        count = len(a)
        print(f"Строка #{ind}: {line}", end='')
        print(f"Кол-во слов в строке #{ind} равно: {count}")

print(f"Суммарное кол-во строк равно: {ind}")

