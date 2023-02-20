db_list = []
def read_db(path:str):
    global db_list
    global past_length
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)

def saved_changes(db):
    data = open('seminars.py\phonebook\database.txt', 'w', encoding= 'UTF-8')
    for dic in range(len(db)):
        count = 0
        cont_count = 0
        for v in db[dic].values():
            count += 1
            if count % 5 == 0 or cont_count == 0:
                data.write(f'\n{v};')
            elif count % 4 == 0:
                data.write(f'{v}')
            else:
                data.write(f'{v};')
            cont_count += 1
    data.close()
  
def detete_contact(db):
    inp = int(input('Введите номер контакта для удаления: '))
    del db[inp - 1]

def change_contact(db):
    inp = int(input('Номер контакта для изменения: '))
    new_contact = {}
    new_contact['lastname'] = input('Введите фамилию: ').title()
    new_contact['firstname'] = input('Введите имя: ').title()
    new_contact['phone'] = input('Введите номер телефона: ')
    new_contact['comment'] = input('Введите комментарий: ').title()
    # new_contact['lastname'] = new_contact['lastname'].title()
    # new_contact['firstname'] = new_contact['firstname'].title()
    # new_contact['comment'] = new_contact['comment'].title()
    db[inp-1] = new_contact

def find(db):
    inp = input('Введите имя, фамилию или номер телефона: ')
    inp = inp.title()
    for dic in range(len(db)):
        for v in db[dic].values():
            if inp == v:
                return db[dic]
    return 'Контакт не найден'

