# Задание 1. Поиск элемента
# Пользователь вводит искомый ключ. Если он хочет, то может ввести
# максимальную глубину — уровень, до которого будет просматриваться
# структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре
# и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
# качестве примера можно использовать такой словарь:
# site = {
# 'html': {
# 'head': {
# 'title': 'Мой сайт'
# },
# 'body': {
# 'h2': 'Здесь будет мой заголовок',
# 'div': 'Тут, наверное, какой-то блок',
# 'p': 'А вот здесь новый абзац'
# }
# }
# }
# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None


site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}


def  searchKey(struct, key, max_depth=None, depth=1):
    result = None
    if max_depth and max_depth < depth:
        return result
    if key in struct:
        return struct[key]
    for subStruct in struct.values():
        if isinstance(subStruct,dict):
            result = searchKey(subStruct,key, max_depth,depth = depth+1)
            if result:
                break
    return result

while True:
    keyInput = input("Введите искомый ключ: ")
    answer = input('Хотите ввести максимальную глубину? Y/N: ')
    if answer.lower() == "y":
        maxDepthInput = int(input('Введите максимальную глубину: '))
    else:
        maxDepthInput = None
    print('Значение ключа:', searchKey(struct=site, key=keyInput, max_depth=maxDepthInput))



