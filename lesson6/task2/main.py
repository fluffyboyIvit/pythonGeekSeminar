
def FillArr():
    arr = []
    size = int(input("Введите размер массива: "))
    for i in range(size):
        arr.append(int(input(f"Введите {i+1} число: ")))
    return arr

def CountNumLessAjacentNum(arr):
    count = 0
    for i in range(1,len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1
    return count

list1 = FillArr()
print(CountNumLessAjacentNum(list1))