def same_by(characteristic, objects):
    ss = set(map(characteristic, objects))
    dd = len(ss)
    return dd == 1