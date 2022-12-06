import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h_max, h_min = [], []
    heapq.heapify(h_max)
    heapq.heapify(h_min)
    cnt = defaultdict(int)
    for i in range(int(input())):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(h_max, -n)
            heapq.heappush(h_min, n)
            cnt[n] += 1
        elif n == 1:
            while h_max:
                num = -heapq.heappop(h_max)
                if cnt[num]:
                    cnt[num] -= 1
                    break
        else:
            while h_min:
                num = heapq.heappop(h_min)
                if cnt[num]:
                    cnt[num] -= 1
                    break
    empty = True
    while h_max:
        num = -heapq.heappop(h_max)
        if cnt[num]:
            empty = False
            break
    if empty:
        print("EMPTY")
    else:
        print(num, end=' ')
        while h_min:
            num = heapq.heappop(h_min)
            if cnt[num]:
                print(num)
                break