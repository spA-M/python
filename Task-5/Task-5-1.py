with open("Text-1.txt", "tw", encoding="utf-8") as my_file:
    a = input("Введите данные построчно: ")
    for el in a.split(' '):
        my_file.write(el + '\n')