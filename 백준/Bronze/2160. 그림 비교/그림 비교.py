N = int(input())
pictures = [''.join([input() for _ in range(5)]) for _ in range(N)]

idx = (0, 0)
min_count = 50
for i in range(N-1):
    for j in range(i+1, N):
        count = sum(pictures[i][k] != pictures[j][k] for k in range(35))
        if count < min_count:
            min_count = count
            idx = (i+1, j+1)
print(*sorted(idx))