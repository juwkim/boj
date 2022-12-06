n = int(input())
s = [*map(int, input())]
a = [s[0]]
for i in range(n-1):
    a += [(s[i] + s[i+1]) % 2]
print(*a, sep='')