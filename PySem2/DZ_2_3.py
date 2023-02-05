# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:   10 -> 1 2 4 8
number_max = int(input('Введите положительное целое число ограничитель: '))
flag, i = True, 0
list_numbers = []
while flag:
    if number_max >= 2**i:
        list_numbers.append(2**i)
        i += 1
    else:
        flag = False
print(f'Числа 2**k ограниченные числом {number_max}: {list_numbers}')
