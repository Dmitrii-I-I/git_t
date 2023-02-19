# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в
# качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1         2         3         4         5          6
# 2         4         6         8         10         12
# 3         6         9         12        15         18
# 4         8        12         16        20         24
# 5        10        15         20        25         30
# 6        12        18         24        30         36
def mult(a: int, b: int) -> int:
    return a*b
def sum(a: int, b: int) -> int:
    return a + b - 2
def int_to_string(number: int) -> str:
    return ('   ' + str(number))[-3:]
def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(num_rows):
        list_0 = list(0 for i in range(num_columns))
        for j in range(num_columns):
            list_0[j] = operation(i + 1, j + 1)
        list_0_srt = map(int_to_string, list_0)
        print(*list_0_srt)

rows = int(input('Ввести кол-во строк: '))
columns = int(input('Ввести кол-во столбцов: '))
if rows == 0 or columns == 0:
    print_operation_table(mult)
else:
    print_operation_table(mult, rows, columns)
