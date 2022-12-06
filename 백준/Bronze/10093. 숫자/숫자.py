A, B = sorted(map(int, input().split()))
print(max(B - A - 1, 0))
print(*range(A+1, B))