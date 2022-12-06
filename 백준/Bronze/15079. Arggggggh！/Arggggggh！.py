n = int(input())
x, y = map(int, input().split())
for _ in range(n-1):
    d, s = input().split()
    s = int(s)
    if d in 'NS':
        y += s * (-1)**'NS'.index(d)
    elif d in 'EW':
        x += s * (-1)**'EW'.index(d)
    elif d in ['NE', 'SW']:
        x += s/2**.5 * (-1)**['NE', 'SW'].index(d)
        y += s/2**.5 * (-1)**['NE', 'SW'].index(d)
    else:
        x += s/2**.5 * (-1)**['SE', 'NW'].index(d)
        y += s/2**.5 * (-1)**['NW', 'SE'].index(d)
print(x, y)