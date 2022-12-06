n, k = int(input()), int(input())
print(1500 * min(n, k + 60) + 3000 * max(n - k - 60, 0))