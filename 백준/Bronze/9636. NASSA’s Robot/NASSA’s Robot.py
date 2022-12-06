from functools import reduce
for _ in range(int(input())):
    move = {s: 0 for s in 'RLUD?'}
    a = reduce(lambda x, y: x.update({y: x.get(y, 0) + 1}) or x, input(), move)
    k = a['?']
    print(a['R'] - a['L'] - k, a['U'] - a['D'] - k, a['R'] - a['L'] + k, a['U'] - a['D'] + k)