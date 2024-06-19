n, m = map(int, input().split())
k = int(input())
ans = 0
if 0 < m < n:
    a, b = 0, 0
    for c in input():
        if c == 'L':
            a += 1; b -= 1
        elif c == 'R':
            a -= 1; b += 1
        a %= 4; b %= 4
        if a != b:
            ans += 1
print(ans)