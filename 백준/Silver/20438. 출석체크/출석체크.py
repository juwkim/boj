import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, K, Q, M = g()
sleep = {*g()}
check = bytearray(N + 3)
for code in g():
    if code not in sleep:
        for num in range(code, N + 3, code):
            if num not in sleep:
                check[num] = 1
ans = [0] * (N + 3)
for i in range(3, N + 3):
    ans[i] = ans[i - 1] + (check[i] == 0)
for _ in range(M):
    S, E = g()
    print(ans[E] - ans[S - 1])