def hourglass():
    rows = 8
    print('|""""""""""|')
    for i in range(int(rows / 2)):
        print(' {}\{}/'.format(' ' * i, ':' * (rows - (2 * i))))
    print('     ||')
    for i in range(int(rows % 5), -1, -1):
        print(' {}/{}\\'.format(' ' * i, ':' * (rows - (2 * i))))
    print('|""""""""""|')

hourglass()
    
