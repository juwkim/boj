import math

N, A, L, R = map(int, input().split())
if A < L * N or A > R * N:
    print("NO")
elif A == 0:
    print("YES")
    print(*[0] * N)
else:
    ans = "YES"
    for w in range(1, N + 1):
        h, r = divmod(A, w)
        if r: continue
        if L <= h <= R:
            w0, h0 = w, h
            break
    else:
        ans = "NO"
    print(ans)
    if ans == "YES":
        print(*[h0] * w0, *[L] * (N - w0))