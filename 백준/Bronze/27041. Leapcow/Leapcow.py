E, L, B = map(int, input().split())
cows = set(int(input()) for _ in range(B))

ans, cur = 0, 0
while cur < E:
    for idx in range(min(E, cur + L), cur, -1):
        if idx not in cows:
            cur = idx
            ans += 1
            break
print(ans)