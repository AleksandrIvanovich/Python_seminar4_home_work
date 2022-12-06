# 1 - Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def give_int(input_string:str):
    while True:
        try:
            num = int(input(input_string))
            if num < 0:
                num = abs(num)
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
            
num = give_int('Введите число:\n') 
          
def get_prime_number (n: int) -> bool:
    for i in range(2,n):
        if not (n % i):
            return False
    return True

prime_num_list = []
for i in range(2,num):
    if not (num % i) and get_prime_number(i) == True:
        prime_num_list.append(i)

print(f'Cписок простых множителей числа {num}: {prime_num_list}')  

    