# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python. 
# Напишите программу, которая выводит на экран все строки этого файла в
# обратном порядке.

text = open("zen.txt",'r')
lines = text.readlines()
text.close()
for line in reversed(lines):
    print(line.strip())

