n = int(input())
for i in range(1, 1 + n):
    for j in range(n//2):
        print(i, (i + j) % n + 1)