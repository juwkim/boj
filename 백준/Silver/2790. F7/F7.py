N, *B = map(int, open(0))
B.sort(reverse=True)
m = max(B[i] + i + 1 for i in range(N))
print(sum(num + N >= m for num in B))