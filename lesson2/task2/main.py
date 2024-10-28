number = int(input("Введите число: "))
n0 = 0
n1 = 0
n2 = 1
i = 2
while n0 < number:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > number:
        i = -1
print(i)
