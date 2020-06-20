"""Задача 2 Данные пользователя"""

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
town = input('Введите город рождения: ')
email = input('Введите свой e-mail: ')
tel = input('Введите свой номер телефона: ')


def info(name, surname, year, town, email, tel):
    a = ' '.join([str("Имя:") + str(name),str("Фамилия:") + str(surname),str("Год рожения:") +  str(year),str("Город рождения:") +  str(town),str("E-mail:") +  str(email),str("Телефон:") +  str(tel)])

    return a

print(f'Пользователь имеет следующие данные: {info(name,surname,year,town,email,tel)}')

