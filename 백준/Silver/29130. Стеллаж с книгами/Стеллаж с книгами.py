n, m = map(int, input().split())
for i in range(n):
    print(*[(3 * i + j) % 5 + 1 for j in range(m)])