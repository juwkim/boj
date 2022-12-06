import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    r1, q1 = divmod(a, n)
    r2, q2 = divmod(b, n)
    ans = n * r1 * r2 + (q1 + 1) * r2 + (q2 + 1) * r1 + max(0, q1 + q2 - n + 1)
    print(ans)