X = int(input())
S = sum(eval(input().replace(' ', '*')) for _ in range(int(input())))
print('Yes' if X == S else 'No')