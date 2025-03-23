import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

S = g()
N = g()
cookie = 0
for _ in range(int(input())):
    cmd, i = g()
    if cmd == 1:
        if all(a >= b * i for a, b in zip(S, N)):
            cookie += i
            S = [a - b * i for a, b in zip(S, N)]
            print(cookie)
        else:
            print("Hello, siumii")
    else:
        S[cmd - 2] += i
        print(S[cmd - 2])