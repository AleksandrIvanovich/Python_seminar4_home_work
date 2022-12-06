# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def give_int(input_string:str):
    while True:
        try:
            num = int(input(input_string))
            if num < 0:
                num = abs(num)
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

def random_list (length_list, down_border, up_border):
   
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list