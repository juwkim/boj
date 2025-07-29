import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    expr = input()
    idx = expr.find('-')
    if idx == -1 or all(expr[i] == '0' for i in range(idx + 3, 2 * N + 1, 2)):
        print("YES")
    else:
        print("NO")