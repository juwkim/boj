g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    A, B, K = g()
    cnt = 0
    for i in range(A):
        for j in range(B):
            cnt += (i & j) < K
    print(f'Case #{_}:', cnt)