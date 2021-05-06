def ask_password():
    for i in range(3):
        if input() == 'password':
            print('Пароль принят')
            break
        elif i == 2:
            print('В доступе отказано')
    return