def int_func():
    a = input('Введите слова с маленькой буквы: ')
    print(f'Исходная строка: {a}')
    a = a.split()
    new_words = []

    for el in a:
        num = ord(el[0])
        new_num = num - 32
        new_letter = chr(new_num)
        new_word = new_letter + el[1:]
        new_words.append(new_word)
        new = " ".join(new_words)
    return new

print (f'Новая строка: {int_func()}')








