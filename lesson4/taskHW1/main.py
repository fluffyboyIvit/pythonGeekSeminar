# Задание 1. Три списка
# Даны три списка.
# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Нужно выполнить две задачи:
# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третьем
# списках.
# Каждую задачу нужно выполнить двумя способами:
# 1. без использования множеств;
# 2. с использованием множеств.
# Пример выполнения на других данных:
# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]
# Вывод:
# Задача 1:
# Решение без множеств: 2
# Решение с множествами: 2
# Задача 2:
# Решение без множеств: 1
# Решение с множествами: 1

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

arrElemInAllArr = []
arrUniqueElem = []
print("без использования множеств: ")
for i in array_1:
    if i in array_2 and array_3:
        arrElemInAllArr.append(i)
    else: arrUniqueElem.append(i)
print("элементы, которые есть в каждом списке: ",arrElemInAllArr)
print("элементы из первого списка, которых нет во втором и третьем: ", arrUniqueElem)

print("с использованием множеств: ")
arrElemInAllArr1 = set()
arrUniqueElem1 = set()
for i in array_1:
    if i in array_2 and array_3:
        arrElemInAllArr1.add(i)
    else: arrUniqueElem1.add(i)
print("элементы, которые есть в каждом списке: ",arrElemInAllArr1)
print("элементы из первого списка, которых нет во втором и третьем: ", arrUniqueElem1)