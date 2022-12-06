from math import ceil
N, K = map(int, input().split())
a, b, c = 0, [0, 0], [0, 0]
for _ in range(N):
    s, y = input().split()
    if y in '12':
        a += 1
    elif y in '34':
        b[int(s)] += 1
    else:
        c[int(s)] += 1
print(sum(map(lambda x: ceil(x/K), [a, *b, *c])))