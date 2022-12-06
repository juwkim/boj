n, m = map(int, input().split())

a, b = 0, 1
for _ in range(n):
    a, b = b % 10, a + b

ans = [a]
for _ in range(m - n):
    a, b = b % 10, a + b
    ans.append(a)
print(*ans, sep='')