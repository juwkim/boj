g = lambda: [*map(int, input().split())]

A = [g() for _ in range(5)]
B = [g() for _ in range(5)]
B = [*zip(*B)]
C = []
for i in range(5):
    tmp = 0
    for j in range(5):
        tmp += sum(x * y for x, y in zip(A[i], B[j]))
    C.append(tmp)
Min = min(range(5), key=lambda x: (C[x], -x))
print(['Inseo', 'Junsuk', 'Jungwoo', 'Jinwoo', 'Youngki'][Min])