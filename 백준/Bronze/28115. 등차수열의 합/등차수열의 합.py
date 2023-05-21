N = int(input())
A = [*map(int, input().split())]
if len(A) <= 2 or len(set(a - b for a, b in zip(A, A[1:]))) == 1:
    print('YES')
    print(*[0] * N)
    print(*A)
else:
    print('NO')