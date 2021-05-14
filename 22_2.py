def partial_sums(*nums):
    res = [0]
    sm = 0
    for el in nums:
        sm += float(el)
        res.append(sm)
    return res