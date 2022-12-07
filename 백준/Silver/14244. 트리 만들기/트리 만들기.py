n, m = map(int, input().split())
buf = [[n - 1] for _ in range(m)]
for i in range(n - 1):
    buf[i % m].append(i)
for l in buf:
    for i in range(len(l) - 1):
        print(l[i], l[i+1])