# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример: 5 -> 1 0 1 1 0      =>  2
import random
number_monets = int(input('Введите кол-во монеток: '))
print('0 - решка, 1 - орел')
list_monets = []
for _ in range(number_monets):
    list_monets.append(random.randint(0, 1))
print(list_monets)
count_reshka = 0
for i in range(number_monets):
    if int(list_monets[i]) == 0: count_reshka += 1
print(count_reshka, number_monets-count_reshka)
if count_reshka == number_monets - count_reshka:
    print(f'Решек и орлов поровну, перверните любые из {count_reshka} монетки')
elif count_reshka == 0:
    print(f'Все {number_monets} монетки лежат орлом вверх')
elif count_reshka == number_monets:
    print(f'Все {number_monets} монетки лежат решкой вверх')
elif count_reshka > number_monets-count_reshka:
    print(f'Необходимо первернуть {number_monets-count_reshka} монетки из {number_monets}, чтобы все монетки былы решкой вверх')
else:
    print(f'Необходимо первернуть {count_reshka} монеток из {number_monets}, чтобы все монетки былы орлом вверх')