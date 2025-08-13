k = int(input())
m = len(pos:=[i for i, c in enumerate(input()) if c == '1'])
print(*[pos[min(m - 1, i + k)] - pos[i] << 1 for i in range(m)])