N, *A = map(int, open(0).read().split())
ans = 0
for l in range(1, N):
    if N % l:
        continue
    num = min(A[:l]) + max(A[:l])
    if all(num == min(A[i:i+l]) + max(A[i:i+l]) for i in range(l, N, l)):
        ans = 1
        break
print(ans)