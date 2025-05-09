import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

while (l:=g())[0]:
    n, m = l
    i, cost = 0, 0
    heads = sorted(int(input()) for _ in range(n))
    for knight in sorted(int(input()) for _ in range(m)):
        if knight >= heads[i]:
            cost += knight
            i += 1
            if i == n:
                print(cost)
                break
    else:
        print("Loowater is doomed!")