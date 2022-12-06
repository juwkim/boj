a, d, k = map(int, input().split())
t = (k-a)/d + 1
print(int(t) if t == int(t) and t > 0 else 'X')