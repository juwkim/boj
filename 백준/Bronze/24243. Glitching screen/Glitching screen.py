g = lambda: [*map(int, input().split())]

h, w, n = g()
stops = [''.join([input() for _ in range(h)]) for _ in range(n)]
check = ''.join([input() for _ in range(h)])
idxes = [i for i in range(len(check)) if check[i] == 'x']

ans = 0
for stop in stops:
    ans += all(stop[idx] == 'x' for idx in idxes)
    if ans == 2:
        break
print('yes' if ans == 1 else 'no')