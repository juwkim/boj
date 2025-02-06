import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    ask, bid = [], []
    s = '-'
    for _ in range(int(input())):
        t, x, _, _, y = input().split()
        x, y = int(x), int(y)
        if t[0] == 's':
            heapq.heappush(ask, (y, x))
        else:
            heapq.heappush(bid, (-y, x))
        while ask and bid and ask[0][0] <= -bid[0][0]:
            a = heapq.heappop(ask)
            b = heapq.heappop(bid)
            s = a[0]
            if a[1] > b[1]:
                a = (a[0], a[1] - b[1])
                heapq.heappush(ask, a)
            elif a[1] < b[1]:
                b = (b[0], b[1] - a[1])
                heapq.heappush(bid, b)
        print(f"{ask[0][0] if ask else '-'} {-bid[0][0] if bid else '-'} {s}")