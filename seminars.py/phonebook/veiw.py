
def main_menu():
    print('Главное меню')
    menu_list =['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Создать контакт', 
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выход'
                ]
    for i in range(len(menu_list)):
        print(f'    {i+1}. {menu_list[i]}')
    user_input = int(input('Введите команду: '))
    return user_input

def show_all(db):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def db_success(db):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()

def create_contact():
    print('Создание нового контакта')
    new_contact = dict()
    new_contact['lastname'] = input('Введите фамилию: ').title()
    new_contact['firstname'] = input('Введите имя: ').title()
    new_contact['phone'] = input('Введите номер телефона: ')
    new_contact['comment'] = input('Введите комментарий: ').title()
    return new_contact

def save_message():
    print('Изменения сохранены')

def delete_message():
    print('Контакт удалён')

def change_message():
    print('Контакт изменён')

def find_contact_message(func):
    print(f'КОНТАКТ НАЙДЕН: {func}')