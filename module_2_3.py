
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
print(f'Список: {my_list} \nПоложительные числа из списка:')

while count < len(my_list):
    num = my_list[count]
    count += 1
    if num == 0:
        continue
    elif num < 0:
        break
    if count == len(my_list):
        print(my_list)
        print('Список закончился')
    else:
        print(num)