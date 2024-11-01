# Задача 3. Сортировка
# Дан список из N чисел. Напишите программу, которая сортирует элементы
# списка по возрастанию и выводит их на экран. Дополнительный список
# использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort
# Постарайтесь придумать и написать как можно более эффективный алгоритм
# сортировки.
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]

list1 = [1,3,-3,0,10]
print("изначальный список: ", list1)
empty = 0 
length = len(list1)
for i in range(len(list1)):
    for j in range(1,length):
        if list1[j] < list1[j-1]:
            empty = list1[j-1]
            list1[j-1] = list1[j]
            list1[j] = empty
    length -= 1
print("Отсортированный список: ", list1)