import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect_left

fibo = [0, 1]
while fibo[-1] < 10**8: fibo.append(fibo[-1] + fibo[-2])
while True:
    W, F, S = g()
    if W == 0:
        break
    cnt = 0
    for num in sorted(fibo[bisect_left(fibo, num)] - num for num in g()):
        if F < num:
            break
        F -= num
        cnt += 1
    print(cnt)