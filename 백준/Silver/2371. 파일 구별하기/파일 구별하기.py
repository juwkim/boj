N = int(input())
buf = [input().split() for _ in range(N)]
K = 1
while len({tuple(l[:K]) for l in buf}) != N:
    K += 1
print(K)