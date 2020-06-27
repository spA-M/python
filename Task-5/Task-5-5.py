with open("Text-5.txt", "w+", encoding="utf-8") as my_file:
    a = input("Введите набор чисел, разделенных пробелами: ")
    my_file.writelines(a)
    number = a.split()
    print(sum(map(int, number)))



