n, a = int(input()), len(input())
ans = 1
for _ in range(n - 1):
    ans = max(ans, min(a, b:=len(input())))
    a = b
print(ans)