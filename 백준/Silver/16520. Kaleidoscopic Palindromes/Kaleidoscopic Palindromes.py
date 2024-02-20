a, b, k = map(int, input().split())
if k == 2:
    ans = 0
    for i in range(a, b + 1):
        c = bin(i)[2:]
        l = len(c)
        ans += all(c[j] == c[l - j - 1] for j in range(l//2))
else:
    t = (0, 1)
    if k == 3:
        t += (6643, 1422773)
    ans = sum(a <= num <= b for num in t)
print(ans)