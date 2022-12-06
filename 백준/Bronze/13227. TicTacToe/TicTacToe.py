a = [input() for _ in range(3)]
a += [''.join(l) for l in zip(*a)] + [a[0][0]+a[1][1]+a[2][2], a[0][2]+a[1][1]+a[2][0]]
print('YES' if 'XXX' in a or 'OOO' in a else 'NO')