class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите числа и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list}')

            except ValueError:
                print(f"Недопустимое значение, вводите только цифры")
                print(f'Для выхода - Q, продолжение - Enter')
                q = input(f"Введите Q или Enter: ")
                if q == 'Q' or q == 'q':
                    print(f'Общий список введенных чисел -\n {self.my_list}')
                    return f'Программа завершена'



try_except = Error(1)
print(try_except.my_input())