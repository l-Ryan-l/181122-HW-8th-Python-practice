from datetime import datetime


def log(option):
    time = datetime.now().strftime('%H:%M:%S')
    with open('log_info.csv', 'a') as logs:
        if option == '1':
            logs.write(f'add new: {time}\n')
        elif option == '2':
            logs.write(f'to show all base: {time}\n')
        elif option == '3':
            logs.write(f'to find employee: {time}\n')
        elif option == '4':
            logs.write(f'log request: {time}\n')
        else:
            logs.write(f'choise out of options. {time}\n')

