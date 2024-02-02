N, k = map(int, input().split())
pos = 0
for i in range(N - 1):
    pos += pos // (k - 1) + 1
print(pos)