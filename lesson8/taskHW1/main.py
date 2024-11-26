# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt
from logger import read_data, write_answer_data

if __name__ == "__main__":
    total_sum = read_data()
    write_answer_data(total_sum)