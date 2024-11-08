
def reverseNum(number):
    if number == 1:
        return input("Введите число: ")
    i = input("Введите число: ")
    res = reverseNum(number-1) + i
    return res
print(reverseNum(int(input("Введите длинну последо-сти: "))))