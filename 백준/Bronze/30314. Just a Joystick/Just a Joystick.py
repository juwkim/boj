N = int(input())
ans = 0
for a, b in zip(input(), input()):
    d = abs(ord(b) - ord(a))
    ans += min(d, 26 - d)
print(ans)