k = int(input("Введите число: "))
list1 = list()

for i in range(k):
    sum = 0
    for j in range(1,i // 2 + 1):
        if i % j == 0:
            sum += j
    list1.append(tuple([i,sum]))

for i in range(len(list1)):
    for j in range(i,len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1]==list1[j][0]:
            print(list1[i])