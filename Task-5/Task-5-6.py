dict = {}

with open(r"C:\BIG DATA\Python Projects\Task-5\text_6.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        subject, lecture, practice, lab = line.split()
        dict[subject] = lecture +' ' + practice +' ' + lab +' '
    print(f'Расписание: {dict}')