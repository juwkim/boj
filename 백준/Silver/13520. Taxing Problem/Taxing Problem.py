import sys
input = sys.stdin.readline

taxs = [[*map(float, input().split())] for _ in range(int(input()))]
P = float(input())
for _ in range(int(input())):
    e, m = map(float, input().split())
    ans, lo = 0, 0
    for s, p in taxs:
        hi = lo + s
        if e < hi:
            cap = hi - max(e, lo)
            net_rate = 1 - p / 100
            max_net = cap * net_rate
            if m <= max_net:
                print(ans + m / net_rate)
                break
            ans += cap
            m -= max_net
        lo = hi
    else:
        print(ans + m / (1 - P / 100))