def read_data():
    numbers_file = open("numbers.txt",'r', encoding='utf-8')
    total_sum = 0

    for line in numbers_file:
        numbers = [int(num) for num in line.split() if num]
        total_sum += sum(numbers)
    numbers_file.close()
    return total_sum
    
def write_answer_data(total_sum):
    sum_file = open("answer.txt", "w", encoding='utf-8')
    sum_file.write(str(total_sum))
    sum_file.close()