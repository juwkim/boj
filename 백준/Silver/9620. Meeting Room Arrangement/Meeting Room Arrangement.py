import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = []
    while True:
        s, f = map(int, input().split())
        if f == 0:
            break
        l.append((s, f))
    l.sort(key=lambda x: x[1])
    ans, prv = 0, -1
    for s, f in l:
        if s >= prv:
            ans += 1
            prv = f
    print(ans)