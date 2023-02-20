import model
import veiw

def start():
    while True:
        user_inp = veiw.main_menu()
        input_handler(user_inp)

def input_handler(inp):
    match inp:
        case 1: # show all contacts
            veiw.show_all(model.db_list)
        case 2: # open file
            model.read_db('seminars.py\phonebook\database.txt')
            veiw.db_success(model.db_list)
        case 8: # exit
            veiw.exit_program()
        case 4: # Create new contact
            model.db_list.append(veiw.create_contact())
        case 3: # Save all changes
            model.saved_changes(model.db_list)
            veiw.save_message()
        case 6: # del contact
            veiw.show_all(model.db_list)
            model.detete_contact(model.db_list)
            veiw.delete_message()
        case 5: # change contact
            veiw.show_all(model.db_list)
            model.change_contact(model.db_list)
            veiw.change_message()
        case 7: # find contact
            veiw.find_contact_message(model.find(model.db_list))

