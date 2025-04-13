import sys
input = sys.stdin.readline

while True:
    n, w = map(int, input().split())
    if n == 0:
        break
    a = [0] * 11
    for _ in range(n):
        a[int(input()) // w] += 1
    cnt = 10
    while cnt and a[cnt] == 0:
        cnt -= 1
    print(sum(a[i] * (cnt - i) for i in range(cnt)) / (cnt * max(a)) + 0.01)