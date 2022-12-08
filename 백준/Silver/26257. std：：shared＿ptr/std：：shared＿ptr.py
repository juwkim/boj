g = lambda: [*map(int, input().split())]
N, M, Q = g()
p = [0] + [int(input()) for _ in range(M)]
for _ in range(Q):
    cmd, *l = input().split()
    if cmd == 'assign':
        a, b = map(int, l)
        p[a] = p[b]
    elif cmd == 'swap':
        a, b = map(int, l)
        p[a], p[b] = p[b], p[a]
    else:
        a = int(l[0])
        p[a] = 0

p = sorted(set(p))
if p[0] == 0:
    p = p[1:]
print(len(p))
for num in p:
    print(num)