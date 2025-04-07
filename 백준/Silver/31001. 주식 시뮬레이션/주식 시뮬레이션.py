import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, Q = map(int, input().split())
groups = defaultdict(list)
cost = {}
for _ in range(N):
    G, H, P = input().split()
    groups[int(G)].append(H)
    cost[H] = int(P)
stocks = defaultdict(int)
for _ in range(Q):
    cmd, *l = input().split()
    cmd = int(cmd)
    if cmd == 6:
        print(M)
    elif cmd == 7:
        print(M + sum(v * cost[k] for k, v in stocks.items()))
    else:
        a, b = l
        b = int(b)
        match cmd:
            case 1:
                if cost[a] * b <= M:
                    stocks[a] += b
                    M -= cost[a] * b
            case 2:
                cnt = min(stocks[a], b)
                stocks[a] -= cnt
                M += cnt * cost[a]
            case 3:
                cost[a] += b
            case 4:
                a = int(a)
                for stock in groups[a]:
                    cost[stock] += b
            case 5:
                a = int(a)
                for stock in groups[a]:
                    cost[stock] = (100 + b) * cost[stock] // 1000 * 10