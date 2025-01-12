P, *A = map(int, open(0))
ans, f = 0, 1
for i in range(P - 1):
    if f:
        if A[i] >= A[i + 1]:
            ans += A[i]
            f = 0
    elif A[i] <= A[i + 1]:
        ans -= A[i]
        f = 1
if f:
    ans += A[-1]
print(ans)