string1  = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split(".")
string2 = ""
for i in string1:
    string2 += str(i)
string2 = string2.lower().split()
res = set(string2)
print(res)
count = 0
for i in range(len(res)):
    count+=1
print(count)
