# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии
# тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

part = 'file_task3.txt'
data = open(part,'r',-1,'utf-8')
new_list = data.read().split('\n')
data.close()

result_list = []
for char in new_list:
    for e in char:
        if e == '5':
            char = char.upper()
    result_list.append(char)

with open('file_task3.2.txt', 'w', -1,'utf-8' ) as data:
    for i in range(len(result_list)):
        data.writelines(f'{result_list[i]}\n')
   
part = 'file_task3.2.txt'
data = open(part,'r',-1,'utf-8')
for line in data:
    print(line,end='')
data.close()    