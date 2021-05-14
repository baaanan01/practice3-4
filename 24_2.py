lst = []
 
while True:
    w = input()
    if w == '':
        break
    lst.append(w)
 
print(*sorted(lst, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')
