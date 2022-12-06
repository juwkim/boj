N, M = map(int, input().split())
a = [i for i in range(1, N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    a = a[:i-1] + a[k-1:j] + a[i-1:k-1] + a[j:]
print(*a)