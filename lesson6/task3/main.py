
def FillArr():
    arr=[]
    size = int(input("Введите размер массива: "))
    for i in range(size):
        arr.append(int(input(f"Введите {i+1} число: ")))
    return arr

def CountNumEqualNumInArr(arr):
    count = 0
    set1 = set()
    for i in range(len(arr)-1):
        if arr[i] in set1:
            continue
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count += 1
                set1.add(arr[i])
    return count

list1 = FillArr()
print(f"кол-во одинаковых чисел: {CountNumEqualNumInArr(list1)}")
