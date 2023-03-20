import sys
input = lambda: sys.stdin.readline().rstrip()
n, q = map(int, input().split())
street = {input(): i for i in range(n)}
for _ in range(q):
    s, e = input().split()
    ans = abs(street[s] - street[e]) - 1
    print(ans)