class View():
    def __init__(self, choice: int = 0):
        self.choice = choice

    def menu(self):
        print('''\nГлавное меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Создать контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить контакт
        8. Выход''')
        while True:
            try:
                self.choice = int(input('Выберите пункт меню: '))
                if 0 < self.choice < 9:
                    return self.choice
                else:
                    print('Введите число от 1 до 8')
            except:
                print('Вводи цифрами, а не буквами!')
    def show_contacts(self, pb: list[dict]):
        if pb == []:
            print('Телефонная книга пуста или файл не открыт!')
        else:
            for i, contact in enumerate(pb, 1):
                name = contact.get('name')
                phone = contact.get('phone')
                comment = contact.get('comment')
                print(f'{i}. {name:20} {phone:<15} {comment:<20}')

    def new_contact_input(self):
        name = input('Введите имя и фамилию: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        new_contact = {'name': name,
                       'phone': phone,
                       'comment': comment}
        return new_contact
    def input_id(self):
        ind = int(input('Введите индекс: '))
        return ind
    def find_contact(self):
        find_str = input('Введите искомый элемент: ')
        return find_str

    def confirm(self, condition: str, name: str):
        answer = input(f'Вы действительно хотите {condition} контакт {name}? (д/н) ')
        if answer == 'д':
            return True
        else:
            return False
    def confirm_changes(self):
        answer = input('У вас есть несохраненные изменения, хотите их сохранить? (д/н) ')
        return True if answer == 'д' else False