import sys
input = sys.stdin.readline

cnt = [0] * 26
pn, pos, d = 0, -1, 1
for _ in range(int(input())):
    cmd, n, *l = input().split()
    n = int(n)
    q, r = divmod(n - pn, 26)
    pn = n
    for i in range(1, 27):
        if i <= r:
            cnt[(pos + i * d) % 26] += q + 1
        else:
            cnt[(pos + i * d) % 26] += q
    pos = (pos + r * d) % 26
    match cmd:
        case 'UPIT':
            x = ord(l[0]) - ord('a')
            print(cnt[x])
        case 'SMJER':
            d = -d