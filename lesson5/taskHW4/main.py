
def printOpenList(lists):
    list1 = []
    for i in lists:
        if isinstance(i, int):
            list1.append(i)
        elif isinstance(i,(list,tuple)):
            list1.extend(printOpenList(i))
    return list1


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
flattenedList = printOpenList(nice_list)
print(flattenedList)