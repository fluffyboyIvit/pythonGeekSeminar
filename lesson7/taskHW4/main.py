# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.

string_input = "Today is a beautiful day! The sun is shining and the birds are singing.".lower()
def coint_uniq_char(string):
    uniq_char =  len(list(filter(lambda x: string_input.count(x.lower()) == 1, string_input)))
    return uniq_char
uniq_count = coint_uniq_char(string_input)
print(uniq_count)