import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, A, B = g()
ans = 0
for p, q in sorted([g() for _ in range(N)], key=lambda x: -abs(x[0] - x[1])):
    if A and B:
        if p < q:
            A -= 1
            ans += p
        else:
            B -= 1
            ans += q
    elif A:
        A -= 1
        ans += p
    else:
        B -= 1
        ans += q
print(ans)