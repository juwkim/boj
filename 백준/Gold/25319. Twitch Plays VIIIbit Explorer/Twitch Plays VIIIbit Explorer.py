g = lambda: [*map(int, input().split())]
N, M, S = g()
buf = {chr(i): [] for i in range(97, 123)}
for i in range(N):
    msg = input()
    for j in range(M):
        buf[msg[j]].append([i, j])

C, L = 0, ''
name = input()
pos_before = (0, 0)

from collections import Counter
a = Counter(name)
b = set(name)
while True:
    if all(len(buf[c]) >= a[c] for c in b):
        C += 1
        for c in name:
            nowx, nowy = pos_before
            x, y = buf[c].pop()            
            if x > nowx:
                L += 'D' * (x - nowx)
            elif x < nowx:
                L += 'U' * (nowx - x)
            if y > nowy:
                L += 'R' * (y - nowy)
            elif y < nowy:
                L += 'L' * (nowy - y)
            L += 'P'
            pos_before = (x, y)
    else:
        break
x, y = N - 1, M - 1
nowx, nowy = pos_before
if x > nowx:
    L += 'D' * (x - nowx)
elif x < nowx:
    L += 'U' * (nowx - x)
if y > nowy:
    L += 'R' * (y - nowy)
elif y < nowy:
    L += 'L' * (nowy - y)
print(C, len(L))
print(L)