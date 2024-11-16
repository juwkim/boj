import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = int(input())
    y = int(input())
    ans = 0
    for _ in range(int(input())):
        sc, rate, cost = input().split()
        sc, rate, cost = int(sc), float(rate), int(cost)
        cur = p
        if sc:
            for _ in range(y):
                cur = int(cur * (1 + rate) - cost)
        else:
            interest = 0
            for _ in range(y):
                interest += int(cur * rate)
                cur -= cost
            cur += interest
        ans = max(ans, cur)
    print(ans)