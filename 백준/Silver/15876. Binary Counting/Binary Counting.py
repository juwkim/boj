g = lambda: [*map(int, input().split())]

s = ''
for i in range(1096):
    s += bin(i)[2:]
    
n, k = g()
for i in range(k-1, k-1 + 5 * n, n):
    print(s[i], end=' ')