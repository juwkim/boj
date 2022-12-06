x = [*map(int, input().split())]
y = [*map(int, input().split())]
print('Y' if all(x[i]^y[i] for i in range(5)) else 'N')