n, w, h = map(int, input().split())
t = [[input() for _ in range(h)] for _ in range(n)]
image = [input() for _ in range(h)]
print(1 + max(range(n), key=lambda i: sum(t[i][j][k] == image[j][k] for j in range(h) for k in range(w))))