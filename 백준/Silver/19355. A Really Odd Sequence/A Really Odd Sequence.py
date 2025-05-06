import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    odd, even = a[0], float('-inf')
    ans = a[0]
    for i in range(1, n):
        odd, even = a[i] + max(0, even), a[i] + odd
        ans = max(ans, odd)
    print(ans)