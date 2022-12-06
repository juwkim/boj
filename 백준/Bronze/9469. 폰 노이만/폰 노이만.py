P = int(input())
for _ in range(P):
    N, D, A, B, F = map(float, input().split())
    print(N, F * D / (A + B))