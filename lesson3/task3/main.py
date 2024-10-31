dict1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]

set1 = set()
for i in dict1:
    for j in i:
        set1.add(i[j])
print(set1)