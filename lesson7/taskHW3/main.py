# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
from collections import Counter
def can_be_poly(string1):
    charCount = Counter(string1)
    result = len(list(filter(lambda x:x%2,charCount.values())))
    return result<2

print(can_be_poly('eerru')) 
print(can_be_poly('abbcba')) 
print(can_be_poly('abbbc')) 