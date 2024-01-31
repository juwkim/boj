import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    L, C, *l = map(int, input().split())
    if L == 0:
        break
    R1, R2 = sorted(l)
    if 2 * R2 > min(L, C):
        print('N')
        continue
    ans = 'N'
    for x, y in ((R2, L - R2), (C - R2, R2), (C - R2, L - R2)):
        if x >= R1 and y >= R1 and (x - R1)**2 + (y - R1)**2 >= (R1 + R2)**2:
            ans = 'S'
            break
    print(ans)