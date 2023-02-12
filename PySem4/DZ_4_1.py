# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:   11 6           2 4 6 8 10 12 10 8 6 4 2         3 6 9 12 15 18       6 12
from random import randint as ri
def random_list(count: int, max_element: int) -> list:
    list_n = []
    for _ in range(count):
        list_n.append(ri(1, max_element))
    return list_n
list_1 = random_list(int(input('Введите количество 1: ')), 20)
list_2 = random_list(int(input('Введите количество 1: ')), 20)
print(f'Список 1: {list_1}')
print(f'Список 2: {list_2}')
set_3 = sorted((set(list_1).intersection(set(list_2))))
if len(set_3) != 0:
    print(f'Список пересечения: {set_3}')
else:
    print('Пересечения списков нет')