from collections import defaultdict

N = int(input())
ans, check = 0, defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    ans += check[a] == b
    check[a] = b

ans += sum(check.values())
print(ans)