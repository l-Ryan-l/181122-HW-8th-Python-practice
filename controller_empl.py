from export_empl import export_dt
from import_empl import import_dt
from search_empl import search_dt
from view_empl import view_dt
from logger import log


def hello_user():
    print('Welcome to corporate data base.\n')


def input_empl():
    surname = input('Enter surname: ')
    first_name = input('Enter name: ')
    birth_date = input('Enter your birth date (dd.mm.yyyy): ')
    phone_number = input('Enter phone number: ')
    position = input('Enter position: ')
    return [surname, first_name, birth_date, phone_number, position]


def sep_choice():
    sep = input('Enter separation symbol: ')
    if sep == '':
        sep = None
    return sep


def main_menu():
    print('Choose option:\n1 - Add employee\n2 - Show all database\n3 - Find employee\n4 - Show logs')
    option = input('Choose option: ')
    log(option)
    if option == '1':
        sep = sep_choice()
        import_dt(input_empl(), sep)
    elif option == '2':
        data = view_dt()
        export_dt(data)
    elif option == '3':
        word = input('Enter data to find: ')
        data = view_dt()
        item = search_dt(word, data)
        if item != None:
            print('Surname'.center(10), 'Name'.center(10), 'Date of Birth'.center(20), 'Phone Number'.center(20), 'Position'.center(20))
            print('*' * 85)
            print(item[0].center(10), item[1].center(10), item[2].center(20), item[3].center(20), item[4].center(20))
        else:
            print('No matches found. Please try again')
    elif option == '4':
        line_count = sum(1 for line in open('log_info.csv'))
        print((f'Number of requests, total: {line_count}'))

    else:
        print('Incorrect data. Try again.\n')
        main_menu()
