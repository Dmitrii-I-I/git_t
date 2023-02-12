# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии. >
def func_pow(osnovanie: None, poradok: int) -> int:
    if poradok == 0:
        return 1
    return osnovanie * func_pow(osnovanie, poradok-1)
osnov = input('Введите число: ')
poradok = int(input('Введите степень числа: '))
osnov = int(osnov)
print(round(func_pow(osnov, poradok), 5))
