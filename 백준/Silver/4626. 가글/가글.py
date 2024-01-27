import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, D, B, E = g()
    ans = []
    s = N % D
    for _ in range(E + 1):
        q, s = divmod(s * 7, D)
        ans.append(q)
    result = "".join(map(str, ans[B:E+1]))
    print(f"Problem set {tc}: {N} / {D}, base 7 digits {B} through {E}: {result}")