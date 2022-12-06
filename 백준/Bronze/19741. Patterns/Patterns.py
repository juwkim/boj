n, k = map(int, input().split())
s = [0] * (n*n)
for i in range(1, 1+n*n):
    for j in range(1, 1+n*n):
        s[j-1] += (j%i == 0)
for i in range(n):
    for j in range(n):
        print('*.'[s[n*i + j] > k], end='')
    print()