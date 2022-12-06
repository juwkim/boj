g = lambda: [*map(int, input().split())]


N, D = g()
A, B = [], []
for _ in range(N):
    *l, t = g()
    if t:
        A.append(l)
    else:
        B.append(l)


ans = 'No'
for i in range(len(A)):
    x, y = A.pop()
    for j in range(len(B)):
        p, q = B[j]
        if (x - p) ** 2 + (y - q) ** 2 == D ** 2:
            ans = 'Yes'
            break
    if ans == 'Yes':
        break
print(ans)