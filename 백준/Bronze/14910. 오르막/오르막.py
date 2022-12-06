n = [*map(int, input().split())]
print('Good' if n == sorted(n) else 'Bad')