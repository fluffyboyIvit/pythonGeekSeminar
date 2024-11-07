def prime(number):
    flag = True
    count = 2
    while count < number and flag:
        if number % count == 0:
            flag = False
        count += 1
    if flag:
        return "yes"
    else:
        return "no"

num = int(input("Введите число: "))
print(prime(num))