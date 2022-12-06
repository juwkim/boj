import heapq
g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    h, l = g()
    buf = []
    for i in range(h):
        for j, order in enumerate(g()):
            if order != -1:
                buf.append((order, i, j))
    heapq.heapify(buf)
    pos = [0] * h
    ans = 0
    while buf:
        order, i, j = heapq.heappop(buf)
        ans += 20 * i + 5 * min((pos[i] - j) % l, (j - pos[i]) % l)
        pos[i] = j
    print(ans)