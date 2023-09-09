import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    ans = 0
    P, C, *S = g()
    while True:
        S.sort(reverse=True)
        if S[C-1] == 0:
            break
        ans += 1
        for i in range(C):
            S[i] -= 1
    print(f"Case #{tc}: {ans}")