import sys
input = sys.stdin.readline
from collections import Counter

while True:
    try:
        cnt, cnt1, cnt2 = Counter(), Counter(), Counter()
        N = int(input())
        P = [[*map(int, input().split())] for _ in range(N)]
        for x, y in P:
            cnt[(x, y)] += 1
            cnt1[x + y] += 1
            cnt2[x - y] += 1
        ans = 0
        for x, y in P:
            ans += cnt1[x + y] + cnt2[x - y] - 2 * cnt[(x, y)]
        print(ans / N / N)
    except:
        break