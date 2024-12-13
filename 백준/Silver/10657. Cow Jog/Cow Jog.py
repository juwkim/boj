a = [int(input().split()[1]) for _ in range(int(input()))]
ans = 1
pv = a.pop()
while a:
    v = a.pop()
    if v <= pv:
        pv = v
        ans += 1
print(ans)