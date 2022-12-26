g = lambda: map(int, input().split())

N, M = g()
ans, prev = 0, 1
for num in g():
    ans += min((prev - num) % N, (num - prev) % N)
    prev = num
print(ans)