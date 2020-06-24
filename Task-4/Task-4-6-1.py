from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1