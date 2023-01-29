# Найдите сумму цифр трехзначного числа.
# Пример:    123 -> 6 (1 + 2 + 3)   100 -> 1 (1 + 0 + 0)
Number = int(input('Введите число: '))
if (Number > 99 and Number < 1000):
    # Решение без цикла
    Summa_number = Number % 10 + Number // 10 % 10 + Number // 100
    print(f'Сумма цифр: {Summa_number}')
else: print('Число не трехзначное')


