N = int(input())
D = int(input())
num, p = 0, 0.5
for c in input()[2:]:
    if c == '1':
        num += p
    p /= 2

ans = []
a, b = 0, 1
for _ in range(N):
    c = a + (b - a) * D / 8
    if num < c:
        ans.append('A')
        b = c
    else:
        ans.append('B')
        a = c
print(*ans, sep='')