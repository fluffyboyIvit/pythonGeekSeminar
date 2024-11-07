# Задача 2. Палиндром
# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом

string1 = (input("Введите строку: "))
letters = {}
uniqueCount = 0
for i in string1:
    letters[i]= letters.get(i,0) + 1

for i in letters:
    if uniqueCount < 2:
        if letters[i] % 2 == 1:
            uniqueCount+=1
    else:
        break
if uniqueCount < 2:
    print("можно сделать полиндромом!")
else:
    print("нельзя сделать полиндромом!")