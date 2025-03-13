N, L = map(int, input().split())
p = [{} for _ in range(14)]
s = input()
for t in range(1, min(N, 14)):
    for i in range(N - t):
        p[t][s[i:i + t]] = s[i + t]
ans = []
for _ in range(L):
    for t in range(13, 0, -1):
        if p[t].get(s[-t:], 0):
            c = p[t][s[-t:]]
            break
    else:
        c = '0'
    ans.append(c)
    for t in range(1, min(len(s), 13) + 1):
        p[t][s[-t:]] = c
    s += c
print(*ans, sep='')