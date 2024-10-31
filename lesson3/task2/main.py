list1 = [5,4,6,7,-10]
k = int(input("введите число: "))
k = k % len(list1)

listRes = []
for i in range(len(list1)-k,len(list1)):
    listRes.append(list1[i])
print (listRes)
for i in range(len(list1)-k):
    listRes.append(list1[i])
print(listRes)