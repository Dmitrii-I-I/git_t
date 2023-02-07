# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100. # Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.
import random
list_number = [random.randint(0, 100) for _ in range(0, int(input('Введите длину списка: ')))]
print(list_number)
number = int(input('Введите искомое число: '))
min_left, min_right = min(list_number), max(list_number)
count = 0
for i in list_number:
    if i == number:
        count += 1
    elif number > i:
        if number-i < number - min_left:
            min_left = i
    elif number < i:
        if i - number < min_right - number:
            min_right = i
if count > 0:
    print(f'Число {number} встречается {count} {"раз" if count == 1 else "раза"}')
else:
    if number > min(list_number):
        print(f'Число {min_left} максимально близко слева для числа {number}')
    if number < max(list_number):
        print(f'Число {min_right} максимально близко справа для числа {number}')