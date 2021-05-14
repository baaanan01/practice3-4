def test(w1, w2):
    a1 = list(w1)
    a2 = list(w2)
    if set(a1) == set(a2):
        return True
    else:
        return False
 
n = int(input())
words = []
for i in range(n):
    word = input().lower()
    if not word in words:
        words.append(word)
words = sorted(words, key=lambda w: w)
while len(words) > 0:
    w = [words.pop(0)]
    k = 0
    while k < len(words):
        w2 = words[k]
 
        if test(w[0], w2):
            w.append(w2)
            words.remove(w2)
        else:
            k += 1
    if len(w) > 1: print(*w)