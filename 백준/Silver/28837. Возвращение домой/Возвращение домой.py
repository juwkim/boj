n, A, B = map(int, input().split())
path = []
for i, a in enumerate(map(int, input().split()), 1):
    if B | a == B and A | a != A:
        path.append(i)
        A |= a
if A == B:
    print(len(path))
    print(' '.join(map(str, path)))
else:
    print(-1)