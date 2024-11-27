tour_data = open('first_tour.txt','r')
tour_data_list = tour_data.readlines()
list_data = []
for line in range(len(tour_data_list)):
    if line == 0:
        minScore = int(tour_data_list[line].strip())
    else:
        list_data.append(list(tour_data_list[line].split()))
second_list = []
count= 0       
for i in list_data:
    for j in range(2,len(i)):
        if int(i[j]) > minScore:
            second_list.append(i)
            count += 1
            

second_tour = open('second_tour.txt','w', encoding='utf-8')
second_tour.write(str(count)+'\n')
for i in second_list:
    j=1
    second_tour.write(f"{j}) {' '.join(i)}\n")
    j+=1
second_tour.close
print(minScore)
print(list_data)
print(second_list)