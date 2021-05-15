import random

strs1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's',
    	't', 'u', 'v', 'w', 'x', 'y']
strs2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y']
strs3 = ['2', '3', '4', '5', '6', '7', '8', '9']
strs4 = strs1 + strs2 + strs3

def generate_password(m):
    maspas = []
    maspas.append(random.choice(strs1))
    maspas.append(random.choice(strs2))
    maspas.append(random.choice(strs3))
    for i in range(0, m - 3):
        maspas.append(random.choice(strs4))
    random.shuffle(maspas)
    return ''.join(maspas)

def main(n, m):
    list_passw = set()
    while len(list_passw) < n:
        list_passw.add(generate_password(m))
    return list_passw