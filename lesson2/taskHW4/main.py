# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника
# за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.

sum = 0
months = 12
for i in range(months):
    sum += int(input(f"Введите зарплату за {i+1} месяц: "))
result = sum / months
print("средняя зарплата за год: ", result)