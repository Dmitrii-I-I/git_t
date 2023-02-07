# Вторая задача:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# ноутбук   -> 12
dict_uk = \
    {
        ('A E I O U L N S T R'): 1,
        ('D G'): 2,
        ('B C M P'): 3,
        ('F H V W Y'): 4,
        ('K'): 5,
        ('J X'): 8,
        ('Q Z'): 10
    }
dict_ru = \
    {
        ('А В Е И Н О Р С Т'): 1,
        ('Д К Л М П У'): 2,
        ('Б Г Ё Ь Я'): 3,
        ('Й Ы'): 4,
        ('Ж З Х Ц Ч'): 5,
        ('Ш Э Ю'): 8,
        ('Ф Щ Ъ'): 10
    }
flag = True
while flag:
    string = input('Введите слово: ')
    string = string.strip()
    string = string.replace(' ', '')
    if not string.isalpha():
        print ('Введены не только буквы, повторите ввод только букв')
    else:
        flag = False
string = string.upper()
if string[0] in str(list(dict_uk.keys())):
    summ_uk = 0
    for letter in string:
        for key in dict_uk:
            if letter in str(key):
                summ_uk += dict_uk.get(key, 0)
    print(f'Стоимость букв UK: {summ_uk}')

def Sum_ru(string):
    if string[0] in str(list(dict_ru.keys())):
        summ_ru = 0
        for letter in string:
            for key in dict_ru:
                if letter in str(key):
                    summ_ru += dict_ru.get(key, 0)
        return ('Стоимость букв RU: ' + str(summ_ru))
if Sum_ru(string) != None:
    print(Sum_ru(string))
