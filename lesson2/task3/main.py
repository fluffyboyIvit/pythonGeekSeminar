numLength = int(input('Введите колличество дней: '))
list1 = []
count = 0
for i in range(numLength):
    list1.append(int(input(f'Введите температуру {i + 1} дня: ')))
    count += 1
print(list1)
count = 0
result = 0
for i in list1:
    if i > 0:
        count += 1
        if count > result:
            result = count
    else:
        count = 0
print(result)