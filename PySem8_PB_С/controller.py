import db_manager
import view

db = db_manager.BookPhone()
message = view.View()
def start():
    while True:
        message.menu()
        match message.choice:
            case 1:
                db.open_file()
                # print(db.book_phone)
            case 2:
                db.save_file()
            case 3:
                book = db.get()
                message.show_contacts(book)
            case 4:
                new = message.new_contact_input()
                db.add(new)
            case 5:
                book = db.get()
                message.show_contacts(book)
                ind = message.input_id()
                db.change_contact(ind, message.edit_contact_input(book, ind))
            case 6:
                find = message.find_contact()
                result = db.find(find)
                message.show_contacts(result)
            case 7:
                pb = db.get()
                message.show_contacts(pb)
                ind = message.input_id()
                name = db.get_name(ind)
                if message.confirm('удалить', name):
                    db.delete_contact(ind)
            case 8:
                if db.check_changes():
                    if message.confirm_changes():
                        db.save_file()
                print('До новых волнующих встреч!')
                break