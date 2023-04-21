input()
ans = 0
for s in input().split():
    a, b = 0, 0
    for c in s:
        if c in 'aeiouy':
            a += 1
        else:
            b += 1
    
    p, q = 0, 0
    for i, c in enumerate(s):
        if i & 1:
            if c in 'aeiouy':
                p += 1
            else:
                q += 1
        else:
            if c in 'aeiouy':
                q += 1
            else:
                p += 1

    ans += min(b, p, q)
print(ans)