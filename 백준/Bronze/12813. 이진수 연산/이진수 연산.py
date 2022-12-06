A, B = input(), input()
res = [[] for _ in range(5)]
g = lambda s, t: res[s].append(str(int(t)))
for x,y in zip(A,B):
    g(0, x == y == '1')
    g(1, '1' in x + y)
    g(2, x != y)
    g(3, 1-int(x))
    g(4, 1-int(y))
print(*map(''.join, res), sep='\n') 