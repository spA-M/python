n = int(input("Введи число: "))

def fact(n):
    for i in range(n):
        yield i + 1

for el in fact(n):
    fac = 1
    i = 1
    while i <= el:
        fac = fac * i
        i = i + 1
    print(f"Факториал {el} равен: {fac}")