dic = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре'}


new_dic = []

with open(r"C:\BIG DATA\Python Projects\Task-5\text_4.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        line = line.split(' ', 1)
        new_dic.append(dic[line[0]] + ' ' + line[1])
    print(new_dic)


with open(r"C:\BIG DATA\Python Projects\Task-5\text_4_NEW.txt", "w", encoding="utf-8") as my_file_new:
    my_file_new.writelines(new_dic)