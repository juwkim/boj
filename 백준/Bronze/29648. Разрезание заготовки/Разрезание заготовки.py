a, b, S = map(int, input().split())
a, b = sorted((a, b))
ans = -1
for i in range(1, int(S**.5) + 1):
    j, r = divmod(S, i)
    if r:
        continue
    if i + b == j + a:
        ans = i + b
        break
print(ans)