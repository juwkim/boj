f = min(int(float(input()) / 0.99), 2)
input()
a, b, c = 0, 0, 0
ans, m = 0, 0
for num in map(int, input().split()):
    m = max(m, num)
    if num:
        a, b, c = a + 1, b + 1, c + 1
    else:
        a, b, c = 0, (0, a + 1)[f > 0], (0, b + 1)[f > 1]
    ans = max(ans, a, b, c)
print(ans)
print(m)