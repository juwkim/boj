g = lambda: [*map(int, input().split())]
n, a, b = g()
off = pow(a, b, 26)
print(*[[chr((ord(i) - off - 65) % 26 + 65), ' '][i == ' '] for i in input()], sep='')