K = int(input())
a = 'G' * K + '.' * (3 * K)
b = '.' * K + 'I' * K + '.' * K + 'T' * K
c = '.' * (2 * K) + 'S' * K + '.' * K
for _ in range(K): print(a)
for _ in range(K): print(b)
for _ in range(K): print(c)