def summa_():
    itog_sum = 0
    quit_prog = False

    while quit_prog == False:
        a = list(input('Введите некоторое количество целых чисел через пробел: ').split())
        summ = 0
        for el in range(len(a)):
            if a[el] == 'q' or a[el] == 'Q':
                quit_prog = True
                break
            else:
                summ = summ + int(a[el])
        itog_sum = itog_sum + summ
        print(f'Текущая сумма элементов равна: {itog_sum}')
    return itog_sum
print(f'Итоговая сумма элементов равна: {summa_()}')
