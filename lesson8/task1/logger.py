from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var  = int(input("В каком формате записать данные: \n \n"
    "1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    "2 вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    "Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int (input("Выберите вариант: "))
    if var == 1 :
        with open('data_first_variant.csv','a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2 :
        with open('data_second_variant.csv','a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('вывожу данные из первого файла: \n')
    with open('data_first_variant.csv','r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))
    print('вывожу данные из второго файла: \n')
    with open('data_second_variant.csv','r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
    
