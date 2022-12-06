N, M = map(int, input().split())
first = ''.join([input() for _ in range(N)])
second = ''.join([input() for _ in range(N)])
print('Not ' * (first != second[::2] or first != second[1::2]) + 'Eyfa')