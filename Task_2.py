# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
import random

def give_int(input_string:str):
    while True:
        try:
            num = int(input(input_string))
            if num < 0:
                 num = abs(num)
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

num_len = give_int("Введите число (количество элементов в списке):\n")           
num_max = give_int("Введите число (максимальный элемент в списке):\n") 

rand_list = []
for i in range(0,num_len):
        rand_list.append(random.randint(1,num_max))
        
result_list = []
for i in rand_list:
     if i not in result_list:
          result_list.append(i)
    
print(rand_list)
print(result_list)
