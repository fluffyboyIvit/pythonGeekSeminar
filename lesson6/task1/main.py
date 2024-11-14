def fillArr():
    listRes=[]
    size = int(input("Введите размер массива: "))
    for i in range(size):
        listRes.append((int(input(f"Введите {i+1} число: "))))
    return listRes

def  FirstElemNotInSecondArr(list1,list2):
    resArr = []
    for i in list1:
        if i not in list2:
            resArr.append(i)
    return resArr

print("Вводим первый массив:")
arr1 = fillArr()
print("Вводим Второй массив:")
arr2 = fillArr()
print(FirstElemNotInSecondArr(arr1,arr2))
