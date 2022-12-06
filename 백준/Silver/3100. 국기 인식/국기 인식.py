from collections import Counter
flags = [input() for _ in range(6)]

ans = 1e10
a = Counter(''.join(flags[:2]))
b = Counter(''.join(flags[2:4]))
c = Counter(''.join(flags[4:]))
for i in range(65, 91):
    for j in range(65, 91):
        if i == j:
            continue
        for k in range(65, 91):
            if k == j:
                continue
            ans = min(ans, 54 - a[chr(i)] - b[chr(j)] - c[chr(k)])

flags = [''.join(l) for l in zip(*flags)]
a = Counter(''.join(flags[:3]))
b = Counter(''.join(flags[3:6]))
c = Counter(''.join(flags[6:]))
for i in range(65, 91):
    for j in range(65, 91):
        if i == j:
            continue
        for k in range(65, 91):
            if k == j:
                continue
            ans = min(ans, 54 - a[chr(i)] - b[chr(j)] - c[chr(k)])
print(ans)