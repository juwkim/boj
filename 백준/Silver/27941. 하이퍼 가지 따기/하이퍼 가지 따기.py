ans = [0] * 11
for l in open(0):
    for i, c in enumerate(l.split()):
        ans[i] ^= int(c)
print(*ans)