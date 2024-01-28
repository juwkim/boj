import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1 << 30
a, b = 1, 0
ans = [0]
for _ in range(1000000):
    a, b = (a + b) % MOD, a
    ans.append(a)
for _ in range(int(input())):
    s, p = map(int, input().split())
    print(ans[s] % (1 << p))