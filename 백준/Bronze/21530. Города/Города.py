n = int(input())
state = ''.join([input() for _ in range(n)])
indexs = [i for i in range(n**2) if state[i] == 'C']
r, q = divmod(indexs[len(indexs) // 2 - 1], n)

for _ in range(r):
    print('1' * n)
print('1' * (q + 1) + '2' * (n - q - 1))
for _ in range(n - r - 1):
    print('2' * n)