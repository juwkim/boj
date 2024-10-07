l, r, x = map(int, input().split())
a = {i | x for i in range(l, r + 1)}
ans = 0
while ans in a:
    ans += 1
print(ans)