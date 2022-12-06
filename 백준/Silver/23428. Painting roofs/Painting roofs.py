g = lambda: map(int, input().split())

m, n = g()
num = 0
for i in range(m):
    s = input()
    for j in range(n):
        num += (int(s[j]) + i + j) & 1
print(min(num, m * n - num))