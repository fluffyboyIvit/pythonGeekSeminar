def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2) #не забывай, что с 0 тоже возвращается 1

number = int(input("введите число: "))

print(fib(number-2))

