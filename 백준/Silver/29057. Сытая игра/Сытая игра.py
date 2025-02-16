g = lambda: [*map(int, input().split())]
D, R = g(), g()
ans = R[0]
while any(ans % d != r for d, r in zip(D, R)):
    ans += D[0]
print(ans)