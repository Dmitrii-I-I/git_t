# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:  4 -> 1 2 3 4     -> 9
from random import randint as ri
flag = True
while flag:
    numbers = int(input('Введите число кустов (не менее 4-х): '))
    if numbers < 4:
        print('Число кустов меньше 4')
    else:
        flag = False
list_berry = dict()
for i in range(numbers):
    list_berry[i] = ri(1, 10)
print(type(list_berry))
print(list_berry)
num_bush = 0
max_berry = 0
# print(list_berry[0])
for bush, berry in list_berry.items():
    if bush == 0:
        count_berry = list_berry[bush] + list_berry[len(list_berry)-1] + list_berry[1]
    elif bush == len(list_berry)-1:
        count_berry = list_berry[bush] + list_berry[bush-1] + list_berry[0]
    else:
        count_berry = list_berry[bush] + list_berry[bush - 1] + list_berry[bush + 1]
    if count_berry > max_berry:
        max_berry = count_berry
        num_bush = bush
print(f'Максимальное кол-во ягод {max_berry} робот соберет у куста {num_bush}')