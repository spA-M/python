a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = [el for el in a if a.count(el) < 2]
print(b)