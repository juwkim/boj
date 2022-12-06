A, B, C = map(int, input().split())
print([A, A^B][C%2])