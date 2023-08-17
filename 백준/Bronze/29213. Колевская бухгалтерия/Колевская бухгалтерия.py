a, b, c = map(int, input().split())
ans = 0
for i in range(c + 1):
    for j in range(i + 1):
        ans += (a + j) > (b + (i - j))
print(ans)