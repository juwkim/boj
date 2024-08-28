import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n, p = map(int, input().split())
    n -= 1
    ans = 0
    while n:
        n &= n - 1
        ans += 1
    print(ans % p)