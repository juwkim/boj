import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

QWERTY = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
idx = {c: (i, j) for i, row in enumerate(QWERTY) for j, c in enumerate(row)}
for _ in range(int(input())):
    s = input()
    ans = len(s)
    for a, b in zip(s, s[1:]):
        i1, j1 = idx[a]
        i2, j2 = idx[b]
        if i1 > i2:
            i1, i2 = i2, i1
            j1, j2 = j2, j1
        ans += 2 * abs(i1 - i2)
        jl, jr = j1 - abs(i1 - i2), j1
        if j2 > jr:
            ans += 2 * (j2 - jr)
        elif j2 < jl:
            ans += 2 * (jl - j2)
    print(ans)