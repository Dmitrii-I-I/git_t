# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as rn
count = int(input('Введите число элементов: '))
list =[]
for i in range(count):
    list.append(rn(-10, 10))
print(*list)
max = int(input('Введите максимум: '))
min = int(input('Введите минимум: '))
if max < min:
    temp = min
    min = max
    max = temp
list_index = []
for i in range(len(list)):
    if list[i] <= max and list[i] >= min:
        list_index.append(i)
print(f'Индексы элементов в диапазоне [{min}, {max}]: {list_index}')