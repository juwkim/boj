g = lambda: [*map(int, input().split())]

w0, l0, T = g()
D, l, A = g()

w = w0 - D * (l0 + A - l)
if w > 0:
    print(w, l0)
else:
    print('Danger Diet')

first = l0
alive = True
for _ in range(D):
    diff = l - l0 - A
    w0 += diff 
    if abs(diff) > T:
        l0 += diff // 2
    
    if w0 <= 0 or l0 <= 0:
        alive = False
        break
if alive:
    if l0 < first:
        print(w0, l0, 'YOYO')
    else:
        print(w0, l0, 'NO')
else:
    print('Danger Diet')