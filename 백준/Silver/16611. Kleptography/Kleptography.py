g = lambda: [*map(int, input().split())]

n, m = g()
key = input()
b = input()
for i in range(m - n, 0, -1):
    key = chr((ord(b[i+n-1]) - ord(key[n-1])) % 26 + 97) + key
print(key)