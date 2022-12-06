import sys
input = sys.stdin.readline
Q, M = map(int, input().split())
res = [1, 1, 2]
a, b = 1, 2
while True:
    a, b = b, (a + b) % M
    res += [*str(b)]
    if a == 1 and b == 1:
        break

for _ in range(Q):
    N = (int(input()) - 1) % (len(res) - 2)
    print(res[N])