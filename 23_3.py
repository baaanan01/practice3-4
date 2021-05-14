strs = input().split(' ')
d = ['а', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
c = 0
check = False
for el in strs:
    i = 0
    for e in el:
        if e in d:
            i += 1
    if c == 0:
        c = i
    else:
        if c != i:
            print('Пам парам')
            check = True

if not check:
    print('Парам пам-пам')