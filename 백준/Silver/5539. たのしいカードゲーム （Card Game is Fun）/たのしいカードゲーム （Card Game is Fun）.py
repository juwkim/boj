A, B, *P = map(int, open(0).read().split())
ans = 0
for start in range(B):
    i, j = 0, start
    while j < B:
        while i < A and P[i] != P[A + j]:
            i += 1
        if i == A:
            break
        i += 1
        j += 1
    ans = max(ans, j - start)
    if ans >= B - start:
        break
print(ans)