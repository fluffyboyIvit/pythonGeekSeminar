# Задача 3. Словарь синонимов
# Одна библиотека поручила вам написать программу для оцифровки словарей
# синонимов. На вход в программу подаётся N пар слов. Каждое слово является
# синонимом для своего парного слова.
# Реализуйте код, который составляет словарь синонимов (все слова в словаре
# различны), затем запрашивает у пользователя слово и выводит на экран его
# синоним. Обеспечьте контроль ввода: если такого слова нет, выведите ошибку
# и запросите слово ещё раз. При этом проверка не должна зависеть от регистра
# символов.
# Пример
# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

length = int(input("Введите кол-во пар слов: "))
database = dict()
for i in range(length):
    first_word, second_word = input(f"{i+1} пара: ").lower().split(" - ")
    if first_word is not database:
        database[first_word] = second_word
        database[second_word] = first_word
flag = False
while flag != True:
    searchWord = input("Введите слово: ").lower()
    if searchWord in database:
        print(database[searchWord])
        flag = True
    else:
        print("такого слова в словаре нет.")