def strtco(A):
        a = A[:1]
        b = A[1:]
        r = int(b)
        c = 'ABCDEFGH'.find(a) + 1
        return (c, r)

def cotost(A):
        (c, r) = A
        return 'ABCDEFGH'[c - 1] + str(r)

def possible_turns(f):
        (x, y) = strtco(f)
        to_output = []
        to_output.append((x + 2, y + 1))
        to_output.append((x + 2, y - 1))
        to_output.append((x - 2, y + 1))
        to_output.append((x - 2, y - 1))
        to_output.append((x + 1, y + 2))
        to_output.append((x - 1, y + 2))
        to_output.append((x + 1, y - 2))
        to_output.append((x - 1, y - 2))
        output = []
        for ((a, b)) in to_output:
            if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
                output += [cotost((a, b))]
        return sorted(output)