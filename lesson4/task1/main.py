string1 = input("Введите строку: ").split()
res = {}
for i in string1:
    if i in res:
        print(f"{i}_{res[i]}", end=" ")
    else:
        print(i, end = " ")
    res[i]= res.get(i,0) + 1
