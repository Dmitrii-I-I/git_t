# from copy import deepcopy
class BookPhone():
    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.book_phone = []
        self.book_phone_first = []

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                # print(type(new))
                # print(new)
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.book_phone.append(new_contact)
                self.book_phone_first.append(new_contact)

    def save_file(self):
        data = []
        for contact in self.book_phone:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def get(self):
        return self.book_phone

    def add(self, new_contact: dict):
        self.book_phone.append(new_contact)

    def find(self, find_option: str):
        all_find = []
        for contact in self.book_phone:
            for element in contact.values():
                if find_option.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind: int, contact: dict):
        self.book_phone.pop(ind-1)
        self.book_phone.insert(ind-1, contact)

    def delete_contact(self, ind: int):
        self.book_phone.pop(ind - 1)

    def get_name(self, ind: int):
        return self.book_phone[ind-1].get('name')

    def check_changes(self):   # class
        if self.book_phone != self.book_phone_first:
            return True
        return False