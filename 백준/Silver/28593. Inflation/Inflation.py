import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
cnt = Counter(map(int, input().split()))
price_sum = sum(k * v for k, v in cnt.items())
inflation = 0
for _ in range(int(input())):
    cmd, x, *y = input().split()
    if cmd[0] == 'I':
        inflation += int(x)
    else:
        real_x = int(x) - inflation
        real_y = int(y[0]) - inflation
        val = cnt[real_x]
        price_sum += cnt[real_x] * (real_y - real_x)
        cnt[real_x] = 0
        cnt[real_y] += val
    print(price_sum + inflation * N)