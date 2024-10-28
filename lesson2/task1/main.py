number = int(input("Введите число: "))
result = number
while number > 1:
    number -= 1
    result = result * number
print(result)