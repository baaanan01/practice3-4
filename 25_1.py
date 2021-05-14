import string
import random
strrs = []
for i in string.ascii_letters:
    if i != "l" and i != "I" and i != "o" and i != "O":
        strrs.append(i)
        random.shuffle(strrs)
for j in string.digits:
    if j != "1" and j != "0":
        strrs.append(j)
        random.shuffle(strrs)

def generate_password(m):
    strs = []
    for i in range(1, m + 1):
        strs.append(str(random.choice(strrs)))
    strs = "".join(strs)
    return strs

def main(n, m):
    sstr = []
    for q in range(1, n + 1):
        sstr.append(generate_password(m))
    return sstr