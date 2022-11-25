def export_dt(data):
    if len(data) > 0:
        print('Surname'.center(10), 'Name'.center(10), 'Date-of-Birth'.center(20), 'Phone-Number'.center(20), 'Position'.center(20))
        print('-' * 85)
        for item in data:
            print(item[0].center(10), item[1].center(10), item[2].center(20), item[3].center(20), item[4].center(20))
    else:
        print('There is no employee for your search.')


