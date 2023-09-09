s = input()
l, n = len(s), int(s)
ans = max(l - 1, 1)
for i in range(1, 10):
    if int(str(i) * l) <= n:
        ans += l
    else:
        ans += l - 1
print(ans)