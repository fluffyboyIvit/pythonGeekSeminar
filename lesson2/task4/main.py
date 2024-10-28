
numLength = int(input('Введите колличество арбузов: '))
list1 = []
count = 0
for i in range(numLength):
    list1.append(int(input(f'Введите вес {i + 1} арбуза: ')))
    count += 1

min = list1[0]
max = list1[0]
for i in list1:
    if i < min:
        min = i
    if i > max :
        max = i
print(min, max)
