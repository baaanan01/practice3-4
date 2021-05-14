strs = input()
ss = 1
while strs:
    try:
        print('Line '+str(ss)+": "+strs.split('#')[1])
    except IndexError: pass
    strs = input()
    ss += 1
