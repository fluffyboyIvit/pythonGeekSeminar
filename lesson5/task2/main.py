def fillInArr(lengthArr):
    list1=[]
    for i in range(lengthArr):
        list1.append(int(input(f"введите {i+1}-ю оценку: ")))
    return list1
def reverseGrade(massive):
    # maxNum = massive[0]
    # minNum = massive[0]
    # for i in massive:
    #     if maxNum< i:
    #         maxNum = i
    #     if minNum>i:
    #         minNum = i
    maxNum = max(massive)
    minNum = min(massive)
    for i in range(len(massive)):
        if massive[i] == maxNum:
            massive[i] = minNum
    return massive


listGrade = fillInArr(int(input("Введите кол-во оценок: ")))
reverseListGrade = reverseGrade(listGrade)
print(reverseListGrade)