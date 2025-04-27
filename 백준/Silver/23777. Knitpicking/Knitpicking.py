from collections import defaultdict

socks = defaultdict(lambda: [0, 0, 0])
total = 0
for _ in range(int(input())):
    t, f, k = input().split()
    k = int(k)
    if f == 'left':
        socks[t][0] += k
    elif f == 'right':
        socks[t][1] += k
    else:
        socks[t][2] += k
    total += k

cnt = sum(max(L, R, 1 if A else 0) for L, R, A in socks.values())
if cnt == total:
    print("impossible")
else:
    print(cnt + 1)