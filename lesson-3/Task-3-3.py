"""Задача 3"""

a = int(input('Введите первый аргумент: '))
b = int(input('Введите второй аргумент: '))
c = int(input('Введите третий аргумент: '))

nums = [a, b, c]

def my_func(a, b, c):

    """Сортируем полученный список по убыванию, если использовать .sort то код будет намного короче"""
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True
    print(f'Список аргументов, отсортированный по убыванию: {nums}')

    """По условию, нам нужны первые два числа в нашем получившемся списке"""
    sum = nums[0] + nums[1]
    return sum

print(f'Сумма наибольших двух аргументов равна: {my_func(a, b, c)}')