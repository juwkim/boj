g = lambda: [*map(int, input().split())]
n, s, k = g()
arr = [0] * n
for num in g():
    arr[(num - 1) // s] += 1

line_len = max(arr)
buf = [('#' * num).ljust(line_len, '.') for num in arr]
print(*[''.join(i) for i in zip(*buf)][::-1], sep='\n')
print('-' * n)