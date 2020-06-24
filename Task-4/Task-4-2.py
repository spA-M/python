from random import randint

b = []
a = []
for el in range(13):
    a.append(randint(0, 300))
print(f"Случайно сформированный список: {a}")
for i in range(len(a)-1):
    if a[i+1] > a[i]:
        b.append(a[i+1])
print(f"Измененный список: {b}")