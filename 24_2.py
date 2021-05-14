def engge():
    lstwrds = []
    for word in iter(input, ''):
        gem = sum(ord(w) - ord('A') + 1 for w in word.upper())
        lstwrds.append([gem, word])
    return sorted(lstwrds)

print(*[w[1] for w in engge()], sep='\n')