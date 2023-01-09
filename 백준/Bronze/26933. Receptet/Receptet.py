ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans += c * max(0, b - a)
print(ans)