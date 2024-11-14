
def mySum (*args):
    totalSum = 0
    for i in args:
        if isinstance(i, int):
            totalSum += i
        elif isinstance(i,(list,tuple)):
            for j in i :
                totalSum += mySum(j)
    return totalSum

print(mySum([[1, 2, [3,4]], [1], 3]))
print(mySum(1, 2, 3, 4, 5))