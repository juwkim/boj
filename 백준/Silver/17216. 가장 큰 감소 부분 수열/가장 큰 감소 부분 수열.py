N = int(input())
A = [*map(int, input().split())]
d = []
for i in range(N):
    d.append(max([0] + [d[j] for j in range(i) if A[i] < A[j]]) + A[i])
print(max(d))