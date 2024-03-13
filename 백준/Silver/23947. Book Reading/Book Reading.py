import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, 1 + int(input())):
    N, M, Q = g()
    check = [0, *[N // i for i in range(1, N + 1)]]
    for P in g():
        for i in range(1, int(P**.5) + 1):
            j, r = divmod(P, i)
            if r:
                continue
            check[i] -= 1
            if i != j:
                check[j] -= 1
    ans = sum(check[num] for num in g())
    print(f'Case #{tc}: {ans}')